
from functools import wraps
from pathlib import Path
from time import time

log_folder = Path(__file__).parent.parent / "logs"
log_folder.mkdir(parents=True, exist_ok=True)
log_file = log_folder / "mylog.txt"
# создание файла mylog.txt в директории logs

def log(filename="mylog.txt") -> None:
    """ Декоратор, который выводит log работы функции и ее результат в файл или консоль. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time()
            result = None
            try:
                result = func(*args, **kwargs)
                time_end = time()
                result_log = f"{func.__name__} ok. Time working: {(time_end - time_start):.6f} seconds. "
            except Exception as e:
                error_log = f"{type(e).__name__}: {e}"
                result_log = f"{func.__name__} error: {error_log}. Input: {args} {kwargs}"
            if filename:
                with open(log_folder / filename, "a", encoding="utf-8") as file:
                    file.write(str(result_log + "\n"))
            else:
                print(result_log)
            return result
        return wrapper
    return decorator

