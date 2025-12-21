import csv
from pathlib import Path
from typing import Union, Dict, List

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

csv_path = DATA_DIR / "transactions.csv"
xlsx_path = DATA_DIR / "transactions_excel.xlsx"
def read_data_from_csv(csv_path: Union[Path,str]) -> List[Dict[str, str]]:
    """ Функция считывания данных из csv файла """
    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            return [dict(row) for row in reader]

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {csv_path} не найден.")

    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV-файла: {e}")

    except Exception as e:
        raise RuntimeError(f"Неизвестная ошибка при чтении CSV: {e}")



def read_data_from_excel(xls_path:Union[Path,str]) -> List[Dict[str, str]]:
    """ Функция считывания данных из xlsx файла """
    try:
        df = pd.read_excel(xls_path)
        return df.astype(str).to_dict(orient="records")

    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден: {xl_path}")

    except Exception as e:
        raise RuntimeError("Неизвестная ошибка при чтении xlsx: {e}")



if __name__ == "__main__":
    print(read_data_from_excel(xlsx_path))
    print(read_data_from_csv(csv_path))
