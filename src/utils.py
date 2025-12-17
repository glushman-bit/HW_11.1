import json
from pathlib import Path
from typing import Optional
import logging

log_folder = Path(__file__).parent.parent / "data"
log_folder.mkdir(parents=True, exist_ok=True)
path = log_folder / "operations.json"


logger = logging.getLogger('utils.log')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_transactions_from_file(path: Optional[str]) -> list[dict]:
    """Получение данных из файла json"""

    operations = []
    try:
        logger.info("открытие файла")
        with open(path, "r", encoding="utf-8") as f:
            try:
                operations = json.load(f)
            except json.JSONDecodeError as er:  # Обработка ошибки если не верный файл
                logger.error(f"Ошибка при чтении файла: {er}")
                return operations

        if not isinstance(operations, list):  # если файл не список
            logger.error("Тип файла не поддерживается")
            return []


    except FileNotFoundError as e:  # если файл не найден
        logger.error(f"Файл не найден {e}")

    return operations


if __name__ == "__main__":
    print(get_transactions_from_file(path))
