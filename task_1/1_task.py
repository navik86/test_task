from collections import defaultdict


def check_relation(net, first, second):
    graph = defaultdict(set)
    visited = set()
    
    # Fill in graph
    for i in net:
        graph[i[0]].add(i[1])
        graph[i[1]].add(i[0])

    # ВFS
    queue = [first]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)

    return True if second in visited else False


if __name__ == '__main__':

    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True