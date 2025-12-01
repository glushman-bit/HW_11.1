from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция, которая фильтрует транзакции по коду валюты."""
    for item in transactions:
        op_currency = item.get("operationAmount", {}).get("currency", {}).get("code")
        if op_currency == currency:
            yield item

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который по очереди выдаёт описание транзакций.
    Если у транзакции нет поля description — пропускает её."""
    for tx in transactions:
        description = tx.get("description")
        if description is not None:
            yield description

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))