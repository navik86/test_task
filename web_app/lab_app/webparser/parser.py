import asyncio
import json
from io import BytesIO

import aiohttp
import openpyxl



def exel_to_list(request):
    file_uploaded = request.FILES.get("file")
    file_name = file_uploaded.name

    if not file_name.endswith(".xlsx"):
        return f"Error. You have uploaded {file_name}"

    try:
        file_data_binary = file_uploaded.read()
        book = openpyxl.open(filename=BytesIO(file_data_binary))
        sheet = book.active
        rows_count = sheet.max_row
        articles = []
        for row_index in range(1, rows_count + 1):
            cell_value = sheet[row_index][0].value
            if isinstance(cell_value, int):
                articles.append(cell_value)
    except Exception:
        return "File data is not valid"
    return articles


async def get_data_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            if resp.status == 200:
                product_data = await resp.text()
                return product_data


def wb_parser(list_of_articles):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    cards_list = []
    for article in list_of_articles:
        task = get_data_from_url(f"https://card.wb.ru/cards/detail?nm={article}")
        cards_list.append(task)
    results = loop.run_until_complete(asyncio.gather(*cards_list))
    result = []
    for i in results:
        parsed = json.loads(i)
        result.append(parsed)
    return result