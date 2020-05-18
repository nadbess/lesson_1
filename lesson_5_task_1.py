with open("task_1.txt", 'w') as my_f:
    while True:
        data = input('enter data or space for exit: ')
        my_f.write(data)
        my_f.write('\n')
        if data == ' ':
            break