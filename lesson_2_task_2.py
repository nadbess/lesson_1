def user_data(name=' ', surname=' ', year=' ', city=' ', email=' ', phone=' '):
    print(f"Имя - {name.capitalize()}; фамилия - {surname.capitalize()}; год рождения - {year}; город - {city.capitalize()}; e-mail - {email}; телефон - {phone}")

user_data(name='иван', year='1986', city='Москва', email='ivan@mail.ru', phone='777-77-77', surname='иванов')
user_data(surname='петров')
user_data(city='СПб', name='петр')