def transformation(line):
    """Принимает строку из значений, раздеденных пробелами, и возвращает список целых чисел до символа 'q' """
    list_line = line.split()
    numbers = []
    for el in list_line:
        try:
            numbers.append(int(el))
        except ValueError:
            break
    return numbers

def sum_of_numbers(numbers):
    """Принимает список и возвращает сумму его чисел.  """
    sum = 0
    for el in numbers:
        sum += el
    return sum

total_sum = 0
sum = 0
user_num = []
print('Для выхода введите "q"')

while True:
    user_input = input('Введите числа, разделяя их пробелом : ')
    user_num = transformation(user_input)
    sum = sum_of_numbers(user_num)
    total_sum += sum
    print('Cумма = ', total_sum)
    if 'q' in user_input:
        break