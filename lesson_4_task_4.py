from random import randint

rand_list = [randint(0, 10) for i in range(20)]
print(rand_list)

new_list = [el for el in rand_list if rand_list.count(el) == 1]
print(new_list)
