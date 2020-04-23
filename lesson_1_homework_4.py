user_number = input('Введите любое число: ')

i=0
numbers = []

while i < len(user_number):
    numbers.append(user_number[i])
    i += 1

print('Наибольшшая цифра из введенного числа: ', max (numbers))
