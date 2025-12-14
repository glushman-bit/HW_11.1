import json
from typing import Optional
from pathlib import Path


log_folder = Path(__file__).parent.parent / "data"
log_folder.mkdir(parents=True, exist_ok=True)
path = log_folder / "operations.json"


def get_transactions_from_file(path: Optional[str]) -> list[dict]:
    """ Получение данных из файла json """

    operations = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                operations = json.load(f)
            except json.JSONDecodeError:  # Обработка ошибки если не верный файл
                print("Mistakes decoder file")
                return operations

        if not isinstance(operations, list): # если файл не список
            print("Type not supported.")
            return []

    except FileNotFoundError: # если файл не найден
        print("File not found")

    return operations


if __name__ == "__main__":
    print(get_transactions_from_file(path))