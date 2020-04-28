my_list = [7, 5, 3, 3, 2]
print('Таблица результатов: ', my_list)
user_rate = int(input('Введите новый результат: '))

i = 0
for i in range(len(my_list)):
        if user_rate >= my_list[i]:
                my_list.insert(i, user_rate)
                break

if user_rate < my_list[i]:
        my_list.append(user_rate)

print(my_list)