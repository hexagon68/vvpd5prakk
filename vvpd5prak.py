import math



def cos_x(x, terms=50):
    """
        Вычисляет значение cos(x) с использованием ряда Маклорена.

        Аргументы:
        x -- значение угла в радианах
        terms (int, optional) -- кол-во членов ряда, используемых для вычисления. По умолчанию 50.
        Возвращаемое значение:
        Значение cos(x)

        Исключения:
        Нет

        Примеры использования:
        >>> cos_x(0)
        1.0
        >>> cos_x(math.pi/2)
        0.0
        """
    res = 0
    for n in range(terms):
        res += ((-1)n * x(2*n)) / math.factorial(2*n)
        return res



def one_plus_x_pow_m(x, m, terms=50):
    """
    Вычисляет значение (1 + x)^m с использованием ряда Маклорена.

    Аргументы:
    x -- значение аргумента
    m -- степень
    terms (int, optional) -- кол-во членов ряда, используемых для вычисления. По умолчанию 50.
    Возвращаемое значение:
    Значение (1 + x)^m

    Исключения:
    -1 < x < 1

    Примеры использования:
    >>> one_plus_x_pow_m(0, 2)
    1.0
    >>> one_plus_x_pow_m(0.1, 3, 5)
    1.331
    """
    if not (-1 < x < 1):
        raise ValueError("x должен быть в пределах -1 < x < 1")
    result = 1
    term = 1
    for n in range(1, terms):
        term *= (m - n + 1) * x / n
        result += term
    return result



def one_minus_x_pow_m(x, m, terms=50):
    """
    Вычисляет значение (1 - x)^m с использованием ряда Маклорена.

    Аргументы:
    x -- значение аргумента
    m -- степень
    terms (int, optional) -- кол-во членов ряда, используемых для вычисления. По умолчанию 50.

    Возвращаемое значение:
    Значение (1 - x)^m

    Исключения:
    -1 < x < 1

    Примеры использования:
    >>> one_minus_x_pow_m(0, 2)
    1.0
    >>> one_minus_x_pow_m(0.1, 2)
    0.81
    """
    if not (-1 < x < 1):
        raise ValueError("x должен быть в пределах -1 < x < 1")

    result = 1
    term = 1
    for n in range(1, terms):
        term *= (m - n + 1) * (-x) / n
        result += term
    return result