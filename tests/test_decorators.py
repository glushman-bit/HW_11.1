import pytest

from src.decorators import my_func, log


def test_decorator_log_correct():
    """Проверка правильности работы декоратора"""
    x = log()(my_func)(1, 2)
    assert x == 3


def test_decorator_log_error(capsys):
    """Проверка на правильность обработки ошибок"""
    with pytest.raises(TypeError, match="TypeError"):
        log(None)(my_func)(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "my_func: TypeError: unsupported operand type(s) for +: 'int' and 'str'\n"
