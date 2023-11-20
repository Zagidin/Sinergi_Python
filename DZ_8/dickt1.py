# Создаём словарь с данными 
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Выводим наш словарь с даными
print(my_dict, "\n")

# Меняем возраст
my_dict["age"] = 26

# Добавляем ключ email со значение "john@example.com"
my_dict["email"] = "john@example.com"

# Удаляем ключ со значение, можно написать my_dict.pop("city")
del my_dict["city"]

# Вывести на экран словарь получившийся по формату примера
print(f'Ключ: {list(my_dict.keys())[0]}, Значение: {my_dict["name"]}\nКлюч: {list(my_dict.keys())[1]}, Значение: {my_dict["age"]}\nКлюч: {list(my_dict.keys())[2]}, Значение: {my_dict["email"]}')
