user_number = int(input('Введите номер месяца: '))

months_list = ['зима', 'весна', 'лето', 'осень']
if user_number <= 2 and user_number > 0 or user_number == 12:
    print(months_list[0])
elif user_number >= 3 and user_number <= 5:
    print(months_list[1])
elif user_number >= 6 and user_number <= 8:
    print(months_list[2])
elif user_number >= 9 and user_number <= 11:
    print(months_list[3])
else:
    print('Число не является номером месяца')

months_dict = {1: 'зима',
               2: 'зима',
               3: 'весна',
               4: 'весна',
               5: 'весна',
               6: 'лето',
               7: 'лето',
               8: 'лето',
               9: 'осень',
               10: 'осень',
               11: 'осень',
               12: 'зима'
               }
print('через dict - ', months_dict.get(user_number))
