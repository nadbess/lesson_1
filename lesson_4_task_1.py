from sys import argv

name, hours, rate, bonus = argv

salary = int(hours) * int(rate) + int(bonus)
print(salary)

