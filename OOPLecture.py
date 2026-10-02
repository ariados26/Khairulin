# Задача №1
# Создай класс Dog.
# У класса должен быть:
# общий атрибут animal_type со значением "Собака";
# конструктор __init__, который принимает имя собаки и сохраняет его в атрибут name;
# метод say_name(), который выводит имя собаки.
# Создай объект класса с именем Бобик и вызови его метод say_name().
from SecondLecture import my_favorite_number


class Dog:
    ANIMAL_TYPE = "Собака"
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(f"{self.name}")
              
my_dog = Dog("Бобик")
my_dog.say_name()

# Задача №2
# Создай класс Car.
# У класса должен быть:
# общий атрибут wheels со значением 4;
# конструктор, который принимает марку автомобиля и сохраняет её в атрибут brand;
# метод show_info(), который выводит марку автомобиля.
# Создай объект для автомобиля Toyota и вызови его метод show_info().

class Car:
    WHEELS = 4
    def __init__(self, brand):
        self.brand = brand
    def show_info(self):
        print(f"{self.brand}")

my_car = Car("Toyota")
my_car.show_info()

# Задача №3
# Создай класс Book.
# У класса должен быть:
# конструктор __init__, который принимает название книги и сохраняет его в атрибут title;
# метод show_title(), который выводит название книги.
# Создай два разных объекта класса Book с названиями:
# "Война и мир"
# "Гарри Поттер"
# Вызови show_title() у обоих объектов.

class Book:
    def __init__(self, title):
        self.title = title
    def show_title(self):
        print(f"{self.title}")
my_favorite_book = Book("Война и мир")
my_second_favorite_book = Book("Гарри Поттер")
my_favorite_book.show_title()
my_second_favorite_book.show_title()

# Задача №4
# Создай класс Student.
# У класса должен быть:
# общий атрибут school со значением "Python School";
# конструктор __init__, который принимает имя ученика и сохраняет его в name;
# метод show_info(), который выводит имя ученика и название школы.
# Создай объект с именем Алексей и вызови show_info().

class Student:
    SCHOOL = "Python School"
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"{self.name}")
        print(f"{self.SCHOOL}")

first_student = Student("Алексей")
first_student.show_info()

# Задача №5
# Создай класс Phone.
# У класса должен быть:
# конструктор __init__, который принимает модель телефона и сохраняет её в model;
# метод call(), который выводит сообщение: Звоню с телефона <модель>.
# Создай объект с моделью Samsung и вызови метод call().

class Phone:
    def __init__(self, model):
        self.model = model
    def call(self):
        print(f"Звоню с телефона {self.model}")
my_phone = Phone("Samsung")
my_phone.call()

# Задача №6
# Создай класс Cat.
# У класса должен быть:
# общий атрибут species со значением "Кошка";
# конструктор __init__, который принимает имя кота и сохраняет его в name;
# метод meow(), который выводит имя кота и слово "Мяу!".
# Создай объект с именем Мурзик и вызови meow().

class Cat:
    SPECIES = "Кошка"
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name}")
        print("Мяу!")
my_cat = Cat("Мурзик")
my_cat.meow()

# Задача №7
# Создай класс BankAccount.
# У класса должен быть:
# общий атрибут bank_name со значением "My Bank";
# конструктор __init__, который принимает имя владельца и начальный баланс и сохраняет их в owner и balance;
# метод show_balance(), который выводит имя владельца и текущий баланс;
# метод deposit(), который принимает сумму и увеличивает баланс на эту сумму.
# Создай объект для владельца Иван с начальным балансом 1000.
# Затем:
# Выведи текущий баланс.
# Пополни счёт на 500.
# Снова выведи баланс.

class BankAccount:
    BANK_NAME = "My Bank"
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def show_balance(self):
        print(f"{self.owner}")
        print(f"{self.balance}")
    def deposit(self, amount):
        amount = int(amount)
        self.balance += amount
client = BankAccount("Иван", 1000)
client.show_balance()
client.deposit(500)
client.show_balance()

# Задача №8
# Создай класс Product.
# У класса должен быть:
# общий атрибут category со значением "Товар";
# конструктор __init__, который принимает название товара и его цену и сохраняет их в name и price;
# метод show_info(), который выводит название и цену товара;
# метод discount(), который принимает размер скидки в процентах и уменьшает цену товара на эту скидку.
# Создай объект товара "Наушники" с ценой 5000.
# Затем:
# Выведи информацию о товаре.
# Сделай скидку 10%.
# Снова выведи информацию о товаре.

class Product:
    CATEGORY = "Товар"
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_info(self):
        print(f"{self.name}")
        print(f"{self.price}")
    def discount(self, discount):
        discount = float(discount)
        self.price -= self.price * (discount / 100)
my_product = Product("Наушники", 5000)
my_product.show_info()
my_product.discount(10)
my_product.show_info()

# Задача №9
# Создай класс Car.
# У класса должен быть:
# общий атрибут wheels со значением 4;
# конструктор __init__, который принимает brand и color и сохраняет их в атрибуты объекта;
# метод show_info(), который выводит марку и цвет автомобиля;
# метод change_color(), который принимает новый цвет и изменяет цвет автомобиля.
# Создай два объекта:
# Toyota, цвет "Белый".
# BMW, цвет "Чёрный".
# Затем:
# Выведи информацию о каждом автомобиле.
# Измени цвет Toyota на "Красный".
# Снова выведи информацию о Toyota.

class Car:
    WHEELS = 4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def show_info(self):
        print(f"{self.brand}")
        print(f"{self.color}")
    def change_color(self, new_color):
        self.color = new_color
first_car = Car("Toyota", "Белый")
second_car = Car("BMW", "Чёрный")
first_car.show_info()
second_car.show_info()
first_car.change_color("Красный")
first_car.show_info()

# Задача №10
# Создай класс Employee.
# У класса должен быть:
# общий атрибут company со значением "IT Company";
# конструктор __init__, который принимает имя сотрудника и его должность и сохраняет их в name и position;
# метод show_info(), который выводит имя, должность и компанию;
# метод promote(), который принимает новую должность и изменяет должность сотрудника.
# Создай объект сотрудника Иван, должность — "Тестировщик".
# Затем:
# Выведи информацию о сотруднике.
# Измени должность на "QA Engineer".
# Снова выведи информацию о сотруднике.

class Employee:
    COMPANY = "IT Company"
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def show_info(self):
        print(f"{self.name}")
        print(f"{self.position}")
        print(f"{self.COMPANY}")
    def promote(self, new_position):
        self.position = new_position
first_employee = Employee("Иван", "Тестировщик")
first_employee.show_info()
first_employee.promote("QA Engineer")
first_employee.show_info()

# Создай класс Counter.
# У класса должен быть:
# общий атрибут start_value со значением 0;
# конструктор __init__, который принимает начальное значение счётчика и сохраняет его в value;
# метод increase(), который увеличивает value на 1;
# метод decrease(), который уменьшает value на 1;
# метод show_value(), который выводит текущее значение.
# Создай два объекта:
# Первый счётчик с начальным значением 5.
# Второй счётчик с начальным значением 10.
# Затем:
# У первого счётчика два раза вызови increase().
# У второго счётчика один раз вызови decrease().
# Выведи значение обоих счётчиков.
# Важно: у объектов значения должны изменяться независимо друг от друга.

class Counter:
    START_VALUE = 0
    def __init__(self, start_value):
        self.value = start_value
    def increase(self):
        self.value += 1
    def decrease(self):
        self.value -= 1
    def show_value(self):
        print(self.value)
first_counter = Counter(5)
second_counter = Counter(10)
first_counter.increase()
first_counter.increase()
second_counter.decrease()
first_counter.show_value()
second_counter.show_value()
