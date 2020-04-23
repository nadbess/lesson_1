cashflow = int(input('Введите вашу прибыль: '))
cost = int(input('Введите ваши издержки: '))

profit = cashflow - cost

if profit > 0:
    print('Ваша выручка ', profit)
    profitability = profit / cashflow
    print('Ваша рентабельность ', profitability)
    stuff = int(input('Введите число сотрудников: '))
    print('Прибыль в расчете на сотрудника: ', profit/stuff)
else:
    print('Убыток')