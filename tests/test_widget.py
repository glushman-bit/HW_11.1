
import pytest
from src.widget import mask_account_card
from src.widget import get_date



""" Проверка корректности распознавания входных данных, проверка с разными типами карт и счетов """
@pytest.mark.parametrize("number_account, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),            # 16-значная карта
    ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ("Card 1234567890123456789", "Card 1234 56** **** ***6 789"),     # 19-значная карта
    ("МояКарта 1234567890", "МояКарта **** **78 90"),                 # 10-значная карта
    ("Счет 12345678901234567890", "Счет **7890"),                     # Счет
    ("сЧеТ 12345678901234567890", "сЧеТ **7890"),                     # Невосприимчивость к регистру
    ("номер счета 98765432109876543210", "номер счета **3210")
])
def test_mask_card_recognition(number_account, expected):
    assert mask_account_card(number_account) == expected

""" Проверка на отсутствие номера """
def test_no_number_present():
    with pytest.raises(ValueError):
        mask_account_card("Просто текст без номера")

""" Проверка на ввод пустой строки """
def test_empty_string():
    with pytest.raises(ValueError):
        mask_account_card("Ничего не введено")

def test_wrong_number_length():
    with pytest.raises(ValueError):
        mask_account_card("Visa 123456")


def test_get_date_origin():
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"

""" Проверка правильности преобразования даты и граничные случаи """
@pytest.mark.parametrize("date, expected",
                         [("2019-07-03T18:35:29.512364", "03.07.2019"),
                          ("0001-01-01T18:35:29.512364", "01.01.0001"),
                          ("9999-12-28T18:35:29.512364", "28.12.9999"),
                          ("2000-02-29T18:35:29.512364", "29.02.2000")])
def test_get_date_present(date, expected):
    assert get_date(date) == expected

""" Проверка на ввод не стандартных дат """
@pytest.mark.parametrize("input_value", [
    "2021/05/17",
    "17-05-2020",
    "2020.05.17",
    "May 17 2020",
    "2020-5-7",        # не ISO-формат
])
def test_get_date_wrong_format(input_value):
    with pytest.raises(ValueError):
        get_date(input_value)

""" Проверка на отсутствие даты """
@pytest.mark.parametrize("input_value", [
    "",
    "   ",
    "date:",
    "not a date",
])
def test_get_date_no_date(input_value):
    with pytest.raises(ValueError):
        get_date(input_value)