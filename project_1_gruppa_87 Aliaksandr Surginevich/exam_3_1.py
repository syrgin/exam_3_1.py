def card_hide():
    card = input("Введите 16 цифр номера вашей кредитной карты ")
    b = card.split()
    for i in b:
        return '************' + i[-4:]


print(card_hide())


def card_hide():
    card = input("Введите 16 цифр номера вашей кредитной карты ")
    return '*' * len(card[:-4]) + card[-4:]


print(card_hide())
