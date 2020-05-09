def my_func_1(x, y):
    """Возводит 1 параметр в степень 2 параметра"""
    return x**y

def my_func_2(x, y):
    """Возводит в степень.

    x: основание
    y: степень
    """
    res = x
    for i in range(y-1):
        res = res * x;
    return res

x = int(input('Введите число основание:'))
y = int(input('Введите число степени:'))

print(my_func_1(x, y))
print(my_func_2(x, y))