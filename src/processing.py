from typing import Iterable

from src.decorators import log


@log()
def filter_by_state(local_list: Iterable[dict], state: str = "EXECUTED") -> list:
    """Функция возвращающая отфильтрованный по статусу список"""
    filtered_list: list = []
    for item in local_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list

if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

@log()
def sorted_by_date(local_list: Iterable[dict], ascending: bool = True) -> list:
    """Функция сортировки по дате"""
    return sorted(local_list, key=lambda item: item.get("date"), reverse=not ascending)

if __name__ == "__main__":
    print(
        sorted_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )