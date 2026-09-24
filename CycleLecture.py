# Задача №1
# Дан список:
from DictionariesLecture import count

numbers = [10, 20, 30, 40]
# С помощью цикла выведи каждый элемент списка на отдельной строке.
for number in numbers:
    print(number)

# Задача №2
# Дан список:
names = ["Alex", "Bob", "Tom"]
# С помощью цикла выведи каждый элемент списка на отдельной строке.
for name in names:
    print(name)

# Задача №3
# Дан список:
fruits = ["apple", "banana", "orange"]
# С помощью цикла for выведи каждый фрукт на отдельной строке.
# Решение не привожу.
for fruit in fruits:
    print(fruit)

# Задача №4
# Дан список:
numbers = [3, 7, 2, 9, 5]
# С помощью цикла выведи каждый элемент списка до тех пор, пока не встретится число 9.
# Число 9 выводить не нужно.
for number in numbers:
    if number == 9:
        break
    print(number)

# Задача №5
# Дан список:
animals = ["cat", "dog", "parrot"]
# С помощью цикла while выведи каждый элемент списка на отдельной строке.
count = 0
while count < len(animals):
    print(animals[count])
    count += 1

# Задача №6
# С помощью range и цикла for выведи числа от 1 до 5 включительно, каждое число на новой строке.
for number in range(1,6):
    print(number)

# Задача №7
# Дан список:
colors = ["red", "green", "blue"]
# С помощью цикла for выведи каждый цвет из списка на новой строке.
for color in colors:
    print(color)

# Задача №8
# Дан список:
numbers = [4, 8, 2, 7]
# С помощью цикла for выведи каждый элемент списка, но не выводи число 2.
for number in numbers:
    if number == 2:
        continue
    print(number)

# Задача №9
# Дан список:
animals = ["cat", "dog", "parrot", "hamster"]
# С помощью цикла for выведи только те элементы, которые не равны "dog"
for animal in animals:
    if animal == "dog":
        continue
    print(animal)

# Задача №10
# Дан список:
numbers = [3, 6, 9, 12]
# С помощью цикла for выведи каждый элемент списка, умноженный на 2.
for number in numbers:
    print(number*2)

# Задача №11
# Дан список:
names = ["Alex", "Bob", "Tom", "Max"]
# С помощью цикла for выведи только те имена, которые содержат букву "o".
for name in names:
    if "o" in name:
        print(name)
# Задача №12
# С помощью for и range выведи числа от 5 до 10 включительно, каждое число с новой строки.
for number in range(5, 11):
    print(number)

# Задача №13
# Дан список:
numbers = [2, 5, 8, 11, 14]
# С помощью цикла for выведи только чётные числа из списка.
for number in numbers:
    if number % 2 == 0:
        print(number)

# Дан список:
fruits = ["apple", "banana", "orange", "pear"]
# С помощью цикла for выведи каждый фрукт с его порядковым номером, начиная с 1.
count = 1
for fruit in fruits:
    print(f'{count} {fruit}')
    count += 1

# Задача №15
# Дан список:
numbers = [4, 7, 2, 9, 5]
# С помощью цикла for найди и выведи первое число, которое больше 6.
# После того как нашёл такое число, цикл должен остановиться.
for number in numbers:
    if number > 6:
        print(number)
        break

# Задача №16
# Дан список:
names = ["Alex", "Bob", "Tom", "Max"]
# С помощью цикла for выведи только имена, длина которых больше 3 символов.
for name in names:
    if len(name) > 3:
        print(name)

# Задача №17
# Дан список:
numbers = [3, 8, 1, 6, 10]
# С помощью цикла for выведи только числа меньше 7.
for number in numbers:
    if number < 7:
        print(number)

# Задача №18
# С помощью for и range выведи чётные числа от 2 до 10 включительно.
for number in range(2, 11):
    if number % 2 == 0:
        print(number)