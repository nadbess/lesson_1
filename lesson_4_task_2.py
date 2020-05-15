from random import randint

my_list = []
i =0
while i < randint(5,10):
    my_list.append(randint(0, 300))
    i += 1
print('Случайный список: ', my_list)

new_list = []
i = 0
while i < (len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])
    i += 1
print('Результат: ', new_list)