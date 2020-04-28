key_1 = 'название'
key_2 = 'цена'
key_3 = 'количество'
key_4 = 'ед. изм.'

key_1_list = []
key_2_list = []
key_3_list = []
key_4_list = []

i = 1
spisok = []

while i < 4:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    value = input('Введите единицу измерения товара: ')

    user = {key_1:name, key_2:price, key_3:quantity, key_4:value}
    key_1_list.append(name.capitalize())
    key_2_list.append(price)
    key_3_list.append(quantity)
    key_4_list.append(value)
    temp_tuple = (i, user)
    spisok.append(temp_tuple)
    i += 1

print(spisok)
data = {key_1:list(set(key_1_list)), key_2:list(set(key_2_list)), key_3:list(set(key_3_list)), key_4:list(set(key_4_list))}
print(data)

