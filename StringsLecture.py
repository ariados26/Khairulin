# Задача №1 — доступ к символам
# Создай строку:
# word = "Python"
# Выведи отдельно:
# первый символ строки;
# последний символ строки.
# Цель: потренировать обращение к символам строки по индексу.

word = "Python"
first_char = word[0]
last_char = word[-1]
print(first_char)
print(last_char)

# Задача №2 — срезы
# Создай строку:
# text = "Automation"
# Получи из неё с помощью среза и выведи отдельно:
# первые 4 символа;
# последние 3 символа.
# Цель: закрепить синтаксис срезов строк.

text = "Automation"
text_first_four_char = text[:4]
text_last_three_char = text[-3:]
print(text_first_four_char)
print(text_last_three_char)

# Задача №3 — получение длины строки
# Создай строку:
# text = "Python Automation"
# Получи длину этой строки и выведи результат.
# Цель: закрепить использование функции len().

text = "Python Automation"
text_length = len(text)
print(text_length)

# Задача №4 — конкатенация строк
# Создай две переменные:
# first_name = "Vadim"
# last_name = "Khairulin"
# Объедини их в одну строку так, чтобы получилось:
# Vadim Khairulin
# Выведи получившуюся строку.
# Цель: закрепить конкатенацию строк с помощью оператора +.

first_name = "Vadim"
last_name = "Khairulin"
full_name = first_name + " " + last_name
print(full_name)

# Задача №5 — базовые методы строк
# Создай строку:
# text = "python"
# Используя метод строки, сделай так, чтобы при выводе получилось:
# PYTHON
# Цель: закрепить вызов базового метода строк.

text = "python"
text_upper = text.upper()
print(text_upper)

# Задача №6 — F-строки
# Создай две переменные:
# name = "Vadim"
# age = 32
# С помощью f-строки выведи сообщение в таком формате:
# Меня зовут Vadim, мне 32 года
# Цель: закрепить синтаксис f-строк и подстановку значений переменных.

name = "Vadim"
age = 32
summary = f"Меня зовут {name}, мне {age} года"
print(summary)

# Задача №7 — создание строки
# Создай переменную greeting со строковым значением, содержащим любое приветствие.
# Затем выведи её значение.
# Цель: закрепить создание строк и присваивание строкового значения переменной.

greeting = "Привет, барсики"
print(greeting)

# Задача №8 — базовые методы строк
# Создай строку:
# text = "   Python   "
# Используя метод строки, убери пробелы в начале и в конце строки.
# Выведи получившийся результат.
# Цель: закрепить ещё один базовый метод строк.

text = "   Python   "
strip_text = text.strip()
print(strip_text)

# Задача №9 — доступ к символам
# Создай строку:
# text = "Automation"
# Выведи отдельно:
# третий символ строки;
# пятый символ строки.
# Цель: закрепить индексацию строк и понять, с какого числа начинается отсчёт индексов.

text = "Automation"
third_char = text[2]
fifth_char = text[4]
print(third_char)
print(fifth_char)

# Задача №10 — срезы
# Создай строку:
# text = "PythonAutomation"
# С помощью среза получи и выведи подстроку:
# Python
# Цель: закрепить указание начала и конца среза строки.

text = "PythonAutomation"
python_text = text[:6]
print(python_text)

# Задача №11 — базовые методы строк
# Создай строку:
# text = "I like Python"
# Используя метод строки, замени слово Python на Selenium.
# Выведи получившуюся строку.
# Цель: закрепить метод replace().

text = "I like Python"
replace_text = text.replace("Python", "Selenium")
print(replace_text)

# Задача №12 — конкатенация строк
# Создай три переменные:
# first = "Python"
# second = "is"
# third = "easy"
# С помощью конкатенации (+) объедини их так, чтобы получилась строка:
# Python is easy
# Выведи результат.
# Цель: закрепить объединение нескольких строк и добавление пробелов между ними.

first = "Python"
second = "is"
third = "easy"
summary_str = first + " " + second + " " + third
print(summary_str)

# Задача №13 — получение длины строки
# Создай строку:
# text = "Automation"
# С помощью len() получи длину строки и проверь, равна ли она 10.
# Выведи результат сравнения.
# Цель: совместить получение длины строки и базовую работу с результатом выражения.

text = "Automation"
length_text = len(text)
print(length_text==10)

# Задача №14 — базовые методы строк
# Создай строку:
# text = "PYTHON"
# Используя метод строки, преобразуй её так, чтобы при выводе получилось:
# python
# Цель: закрепить метод изменения регистра строки.

text = "PYTHON"
lower_text = text.lower()
print(lower_text)

# Задача №15 — F-строки
# Создай две переменные:
# name = "Vadim"
# language = "Python"
# С помощью f-строки сформируй и выведи предложение:
# Vadim изучает Python
# Цель: закрепить подстановку нескольких переменных в одну строку.

name = "Vadim"
language = "Python"
summary_speaking = f"{name} изучает {language}"
print(summary_speaking)

# Задача №16 — базовые методы строк
# Создай строку:
# text = "Python Automation"
# С помощью метода строки проверь, содержит ли строка слово "Python".
# Выведи результат проверки.
# Цель: закрепить ещё один базовый метод строк, который позволяет искать подстроку.

text = "Python Automation"
text_result = text.find("Python")
print(text_result)

# Задача №17 — срезы
# Создай строку:
# text = "Python Automation"
# С помощью среза получи и выведи только слово:
# Automation
# Цель: закрепить срез строки, начиная с нужного индекса и до конца строки.

text = "Python Automation"
text_second_word = text[7:17]
print(text_second_word)