user_str = input('Введите несколько слов, разделяя их пробелами: ')
words = user_str.split()
for ind, el in enumerate(words, 1):
    print(ind, el[:10])