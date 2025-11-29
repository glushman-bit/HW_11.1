def get_mask_card_number(number_card: str, mask_char: str = "*", group_size: int = 4) -> str:
    # Проверяем что номер состоит из цифр
    if not number_card.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    length = len(number_card)
    # Исключаем номера не верной длинны
    if length not in (10, 16, 19):
        raise ValueError("Неверная длина номера карты")
    if length == 0:
        raise ValueError("Ничего не введено")
    # Маскировка номера длинной 10
    if length == 10:
        mask_section = mask_char * (len(number_card) - 4)
        mask_number = mask_section + number_card[-4:]
    # Маскировка номеров длинной 16 и 19
    else:
        mask_section = mask_char * (len(number_card) - 10)
        mask_number = number_card[:6] + mask_section + number_card[-4:]
    # Группировка номера
    group_number = " ".join([mask_number[i: i + group_size] for i in range(0, len(mask_number), group_size)])
    return group_number


def get_mask_account(number_account: str, mask_char: str = "*") -> str:
    """Функция, скрывающая номер банковского счета"""
    if not number_account.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    mask_part = mask_char * 2
            # указывает сколько символов перед открытым номером
    mask_number = mask_part + number_account[-4:]

    if len(number_account) != 20:
        raise ValueError("Введен не верный номер")

    return mask_number

