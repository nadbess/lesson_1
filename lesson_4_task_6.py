from itertools import count
from itertools import cycle


for el in count(3):
    if el > int(10):
        break
    else:
        print(el)

numbers = [10, 20, 30, 40, 50]
iter = cycle(numbers)
i = 0
while i < len(numbers):
    print(next(iter))
    i += 1



