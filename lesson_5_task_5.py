with open('task_5.txt', 'w') as my_f:
    print('4 15 25 13 89', file=my_f)
sum = 0
with open('task_5.txt') as my_f:
    line = my_f.read()
    numbers = line.split()
    for el in numbers:
        sum += int(el)
print(sum)