def my_func(par_1, par_2, par_3):
    """Возвращает сумму двух наибольших параметров. """
    sum_1 = par_1 + par_2
    sum_2 = par_2 + par_3
    if sum_1 > sum_2:
        return sum_1
    else:
        return sum_2

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

print('Сумма двух наибольших чисел =', my_func(x, y, z))