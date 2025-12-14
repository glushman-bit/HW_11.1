import json
import pytest
from unittest.mock import mock_open, patch

from src.utils import get_transactions_from_file




@pytest.mark.parametrize("read_data, side_effect, expected",
    [
        # 1. Корректный JSON-файл → список словарей
        (json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]), None, [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]),
        # 2. Пустой файл → JSONDecodeError → []
        ("", None, []),
        # 3. Файл не найден → []
        (None, FileNotFoundError, []),
        # 4. JSON, но не список → []
        (json.dumps({"id": 1, "amount": 100}), None, [])
    ]
                         )

def test_get_transactions_from_file_parametrized(read_data, side_effect, expected):
    if side_effect:
        with patch("builtins.open", side_effect=side_effect):
            result = get_transactions_from_file("operations.json")
    else:
        with patch("builtins.open", mock_open(read_data=read_data)):
            result = get_transactions_from_file("operations.json")

    assert result == expected

