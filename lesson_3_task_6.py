def int_func_capitalize(word):
    return word.capitalize()

def int_func_title(word):
    return word.title()

def int_func_cycle(word):
    word_list = word.split()
    new_sentence = ''
    for el in word_list:
        new_sentence = new_sentence + int_func_capitalize(el)+' '
    return new_sentence


sentence = input('Введите несколько слов, разделенных пробелами: ')

print(int_func_capitalize(sentence) + ' решение через capitalize')
print(int_func_title(sentence) + ' решение через title')
print(int_func_cycle(sentence) + 'решение через ранее написанную функцию')