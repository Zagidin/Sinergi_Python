age, maintainer = int(input('Введите возраст: ')), input('Есть ли сопровождающий [Да / Нет] -> ')

if age < 12:
    print("Билет бесплатный")
elif 12 <= age <= 18 and maintainer == 'Да':
    print("Билет со скидкой")
else:
    print("Полная стоимость билета")
