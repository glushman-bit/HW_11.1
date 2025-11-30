from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция, которая фильтрует транзакции по коду валюты."""
    for item in transactions:
        op_currency = item.get("operationAmount", {}).get("currency", {}).get("code")
        if op_currency == currency:
            yield item