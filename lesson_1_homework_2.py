user_number = int(input('Введите число секунд: '))

hour = user_number // 3600
minute = (user_number - hour*3600) // 60
second = user_number - hour * 3600 - minute * 60

print(f"{user_number} секунд составляет {hour} час(ов), {minute} минут(ы) и {second} секунд(ы).")