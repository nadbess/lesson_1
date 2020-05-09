def divide_func():
    """" Запрашивает данные и возращает результат деления.

    x - делимое
    y - делитеть
    """
    try:
        x = int(input('Введите делимое: '))
        y = int(input('Введите делитель: '))
        return round(x / y, 2)
    except ZeroDivisionError:
        return

print(divide_func())