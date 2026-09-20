# Задача №1
# Создай словарь person с двумя ключами:
# "name" — значение "Vadim"
# "age" — значение 25
# После этого выведи на экран значение ключа "name".
from itertools import count

person = {
    "name": "Vadim",
    "age": 25,
}
print(person["name"])

# Задача №2
# Дан словарь:
# car = {
#     "brand": "Toyota",
#     "year": 2020,
# }
# Добавь в него новый ключ "color" со значением "black".
# После этого выведи весь словарь на экран.

car = {
    "brand": "Toyota",
    "year": 2020,
}
car["color"] = "black"
print(car)

# Задача №3
# Дан словарь:
# student = {
#     "name": "Alex",
#     "age": 20,
#     "city": "Berlin",
# }
# Измени значение ключа "age" на 21.
# После этого выведи значение "age" на экран.

student = {
    "name": "Alex",
    "age": 20,
    "city": "Berlin"
}
student["age"] = 21
print(student["age"])

# Задача №4
# Дан словарь:
# fruits = {
#     "apple": 3,
#     "banana": 5,
#     "orange": 2,
# }
# Удалить из словаря ключ "banana".
# После этого выведи весь словарь на экран.

fruits = {
    "apple": 3,
    "banana": 5,
    "orange": 2,
}
del fruits["banana"]
print(fruits)

# Задача №5
# Дан словарь:
person = {
    "name": "Vadim",
    "age": 25,
    "city": "Berlin",
}
# Выведи на экран все ключи этого словаря.

print(person.keys())

# Задача №6
# Дан словарь:
user = {
    "name": "Alex",
    "age": 25,
    "city": "Berlin",
}
# Проверь, есть ли в словаре ключ "age".
# Если есть — выведи:
# Ключ существует
# Если нет — выведи:
# Ключа нет

if "age" in user:
    print("Ключ существует")
else:
    print("Ключа нет ")

# Задача №7
# Дан словарь:
person = {
    "name": "Vadim",
    "age": 25,
    "city": "Berlin",
}
# Выведи на экран все значения этого словаря.

print(person.values())

# Задача №8
# Дан словарь:
book = {
    "title": "Python",
    "pages": 300,
    "author": "Alex",
}
# Получи и выведи на экран все пары ключ–значение этого словаря.
print(book.items())

# Задача №9
# Дан словарь:
user = {
    "name": "Alex",
    "age": 30,
    "city": "Berlin",
}
# Проверь, есть ли значение "London" среди значений словаря.
# Если есть — выведи:
# Город найден
# Если нет — выведи:
# Города нет

if "London" in user.values():
    print("Город найден")
else:
    print("Города нет")

# Задача №10
# Дан словарь:
product = {
    "name": "Laptop",
    "price": 1000,
}
# Добавь в словарь ключ "price" со значением 1200, чтобы обновить существующее значение.
# После этого выведи весь словарь на экран.

product["price"] = 1200
print(product)

# Задача №11
# Дан словарь:
colors = {
    "red": "красный",
    "blue": "синий",
    "green": "зелёный",
}
# Получи и выведи на экран значение ключа "blue".
print(colors["blue"])

# Задача №12
# Дан словарь:
user = {
    "name": "Alex",
    "age": 25,
}
# Добавь в словарь новый ключ "city" со значением "Berlin".
# После этого выведи только значение нового ключа "city".

user["city"] = "Berlin"
print(user["city"])

# Задача №13
# Дан словарь:
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
}
# Удалить из словаря ключ "two".
# После этого проверь, существует ли ключ "two" в словаре.
# Если существует — выведи:
# Ключ существует
# Если нет — выведи:
# Ключа нет

del numbers["two"]
if "two" in numbers:
    print("Ключ существует")
else:
    print("Ключа нет")

# Задача №14
# Дан словарь:
student = {
    "name": "Alex",
    "age": 20,
    "city": "Berlin",
}
# Выведи на экран количество элементов (пар ключ–значение) в словаре.

count = len(student.keys())
print(count)

# Задача №15
# Дан словарь:
person = {
    "name": "Vadim",
    "age": 25,
    "city": "Berlin",
}
# Проверь, есть ли в словаре значение 25.
# Если есть — выведи:
# Возраст найден
# Если нет — выведи:
# Возраст не найден

if 25 in person.values():
    print("Возраст найден")
else:
    print("Возраст не найден")

# Задача №16
# Дан словарь:
phone = {
    "brand": "Samsung",
    "model": "Galaxy",
    "year": 2024,
}
# Удали из словаря ключ "year".
# После этого выведи все ключи оставшегося словаря.

del phone["year"]
print(phone.keys())

# Задача №17
# Дан словарь:
user = {
    "name": "Alex",
    "age": 25,
    "city": "Berlin",
}
# С помощью assert проверь, что в словаре существует ключ "age".
# Если ключ существует — программа должна продолжить выполнение без ошибки.

assert "age" in user.keys()

# Задача №18
# Дан словарь:
car = {
    "brand": "BMW",
    "model": "X5",
    "year": 2022,
}
# С помощью assert проверь, что значение ключа "brand" равно "BMW".
# Решение не привожу.

assert car["brand"] == "BMW"

# Задача №19
# Дан словарь:
student = {
    "name": "Alex",
    "age": 20,
    "city": "Berlin",
}
# С помощью assert проверь, что значение "Berlin" присутствует среди значений словаря.
# Решение не привожу.

assert "Berlin" in student.values()

# Задача №20
# Дан словарь:
product = {
    "name": "Laptop",
    "price": 1000,
    "brand": "Lenovo",
}
# С помощью assert проверь, что в словаре существует ключ "price".
# Решение не привожу.

assert "price" in product.keys()
