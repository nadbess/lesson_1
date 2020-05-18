lines = 0
words = 0
letters = 0

with open('task_2.txt', 'r') as my_f:
    for line in my_f:
        lines += 1
        letters += len(line)

        pos = 'out'
        for letter in line:
            if letter != ' ' and pos == 'out':
                words += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'

print(f'Строк - {lines}, слов - {words}, букв - {letters}')