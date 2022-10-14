import json

from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .pydantic_model import Validator
from .serializers import InputSerializer
from .parser import exel_to_list, wb_parser


class ParserView(GenericViewSet):
    serializer_class = InputSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        art = 0
        cards = []
        list_of_articles = []
        up_file = request.FILES.get("file")
        article = request.data["article"]
        if up_file is None and article == "":
            return Response("Выберите файл или введите артикул")
        elif up_file is None:
            list_of_articles.append(article)
        else:
            list_of_articles = exel_to_list(request)
        wb_full_list = wb_parser(list_of_articles)

        for i in wb_full_list:
            if i["data"]["products"] == []:
                wb = [{
                    "id": f"{list_of_articles[art]}",
                    "name": "Нет информации по артикулу",
                    "brand": "Нет информации по артикулу"
                }]
            else:
                wb = i["data"]["products"]
            art += 1
            data = json.dumps(*wb, ensure_ascii=False)
            try:
                card = Validator.parse_raw(data)
                card_json = json.loads(card.json(ensure_ascii=False, ))
                cards.append(card_json)
            except ValidationError as e:
                return Response({e.json()})

        return Response([c for c in cards])