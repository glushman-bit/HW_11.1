from functools import wraps
from pathlib import Path
from datetime import datetime
from typing import Callable, Optional

log_folder = Path(__file__).parent.parent / "logs"
log_folder.mkdir(parents=True, exist_ok=True)
log_file = log_folder / "mylog.txt"
# создание файла mylog.txt в директории logs


def write_to_file(content: str, log_file: Optional[str]) -> None:
    if log_file:
        with open(log_file, "a", encoding="utf-8") as file:
            file.write(content + "\n")
    else:
        print(content)

def log(filename: Optional[str]=log_file) -> Callable:
    """ Декоратор, который создает log-и на работу функции и ее результат в файл или консоль. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            try:
                result = func(*args, **kwargs)
                time_end = datetime.now()
                result_log = f"{func.__name__} ok. Start: {time_start}. Time working: {time_end - time_start} seconds. "
                write_to_file(result_log, filename)
                return result
            except Exception as e:
                error_log = f"{type(e).__name__}: {e}"
                write_to_file(error_log, filename)
                raise
        return wrapper
    return decorator

@log
def my_func(x, y):
    """ Функция для проверки декоратора """
    return x + y

