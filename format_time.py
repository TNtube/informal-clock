import time

t = tuple(map(int, time.strftime("%H %M").split()))


def format_minute(minute: int) -> str:
    """
    Formatte un entier pour en donner une forme utilisable avec un dictionnaire
    :param minute: les minutes, un entier
    :return: un string, les minutes une fois formattés
    >>> format_minute(15)
    'et quart'
    >>> format_minute(30)
    'et demie'
    >>> format_minute(45)
    'moins le quart'
    >>> format_minute(0)
    ''
    >>> format_minute(37)
    'moins vingt-cinq'
    """

    form = {0: '', 5: 'cinq2', 10: 'dix2', 15: 'et quart', 20: 'vingt',
            25: 'vingt cinq2', 30: 'et demie', 35: 'moins vingt cinq2',
            40: 'moins vingt', 45: 'moins le quart', 50: 'moins dix2',
            55: 'moins cinq2', 60: None}

    dizaine, unit = divmod(minute, 10)

    if unit in range(0, 3):
        unit = 0
    elif unit in range(3, 8):
        unit = 5
    else:
        unit = 0
        dizaine += 1

    return form[dizaine * 10 + unit]


def format_hour(hour: int, minute: int) -> str:
    """
    Retourne l'heure écrit de manière formelle
    :param hour: un entier, les heures
    :param minute: un entier, les minutes
    :return: une chaine de caractère, l'heure de manière formelle
    >>> format_hour(15, 28)
    'Il est trois heures et demi'
    >>> format_hour(0, 24)
    'Il est minuit vingt-cinq'
    """
    form = {0: 'minuit', 1: "une heure", 2: 'deux heures', 3: 'trois heures',
            4: 'quatre heures', 5: 'cinq heures', 6: 'six heures', 7: 'sept heures',
            8: 'huit heures', 9: 'neuf heures', 10: 'dix heures', 11: 'onze heures',
            12: 'midi'}

    minutes = format_minute(minute)
    if minutes is None or minutes.startswith("moins"):
        hour += 1
    if minutes is None:
        minutes = ''
    if hour == 24:
        hour = 0
    elif hour > 12:
        hour -= 12

    return f"Il est {form[hour]} {minutes}".upper()


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())


