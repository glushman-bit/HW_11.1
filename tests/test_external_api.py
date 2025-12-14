from unittest.mock import Mock
from unittest.mock import patch

import pytest

from src.external_api import converter_currency


@patch("requests.get")
def test_converter_currency_right(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 79.67}
    mock_get.return_value = mock_response

    result = converter_currency(1, "USD")

    assert result == 79.67

    mock_get.assert_called_once()


def test_converter_currency_invalid_currency():
    with pytest.raises(ValueError, match="Код валюты не поддерживается"):
        converter_currency(100, "GBP")


@patch("requests.get")
def test_converter_currency_http_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    with pytest.raises(Exception, match="Ошибка запроса: 500"):
        converter_currency(1, "USD")


def test_converter_currency_invalid_transaction():
    with pytest.raises(ValueError, match="Введена неверная сумма транзакции"):
        converter_currency("1", "USD")


def test_converter_currency_negative_transaction() -> None:
    with pytest.raises(ValueError, match="Сумма транзакции не может быть отрицательной"):
        converter_currency(-1, "USD")
