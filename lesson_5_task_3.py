total_salary = 0.00
lines = 0

with open('task_3.txt') as my_f:
    for line in my_f:
        name_salary = line.split()
        if float(name_salary[1]) > 20000:
            print(name_salary[0])
        total_salary += float(name_salary[1])
        lines += 1

average_salary = round(total_salary/lines, 2)
print(average_salary)