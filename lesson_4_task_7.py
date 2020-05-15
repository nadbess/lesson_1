def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    yield res

for el in factorial(4):
    print(el)