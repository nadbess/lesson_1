from functools import reduce

rand_list = [el for el in range(100, 1001) if el % 2 == 0 ]
print(rand_list)

res = reduce(lambda x,y: x * y, rand_list)
print(res)