# Урок 5: Функции в Python
# Функции — это важный аспект программирования, который помогает организовывать код и повышать его читаемость. Давай рассмотрим основные концепции функций в Python.
#
# 1. Зачем нужны функции?
# Повторное использование кода: Функции позволяют избежать дублирования кода. Например, если вам нужно несколько раз выполнить одну и ту же задачу, вы можете написать функцию один раз и вызывать её каждый раз, когда это необходимо.
# Организация кода: Функции помогают разбивать код на логические блоки, что делает его более структурированным и понятным.
# Упрощение отладки: Легче тестировать и исправлять ошибки в небольших функциях, чем в больших блоках кода.

# 2. Определение и вызов функции
# Синтаксис определения функции:
def имя_функции(параметры):
    # тело функции
    return результат  # возвращает значение (опционально)

# Пример функции:
def greet(name):
    print("Hello,", name)

# Вызов функции
greet("Andrii")  # Вывод: Hello, Andrii

# Здесь мы определили функцию greet, которая принимает параметр name и выводит приветственное сообщение.
#
# 3. Возврат значений
# Функции могут возвращать значения с помощью ключевого слова return. Это позволяет сохранять результат выполнения функции и использовать его в других частях программы.
#
# Пример возврата значения:

def add(a, b):
    return a + b

result = add(3, 5)
print("Сумма:", result)  # Вывод: Сумма: 8

# Здесь функция add принимает два параметра, складывает их и возвращает результат.
#
# 4. Аргументы и параметры
# Параметры — это переменные, указанные в определении функции.
# Аргументы — это фактические значения, которые вы передаете функции при ее вызове.
# Пример:

def multiply(x, y):
    return x * y

product = multiply(4, 5)  # 4 и 5 — аргументы
print("Произведение:", product)  # Вывод: Произведение: 20

# 5. Функции с переменным числом аргументов
# Вы можете использовать *args и **kwargs для передачи переменного числа аргументов в функцию.
#
# *args позволяет передавать неограниченное количество позиционных аргументов.
# **kwargs позволяет передавать неограниченное количество именованных аргументов.
# Пример с *args:

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Вывод: 15

# Пример с **kwargs:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Andrii", age=32, city="Saint Petersburg")

# Домашнее задание

# Создай функцию factorial:
#
# Функция должна принимать одно число и возвращать его факториал, используя цикл while.
# Если число отрицательное, функция должна возвращать сообщение: "Факториал для отрицательных чисел не определён."
# Создай функцию is_even:
#
# Эта функция должна принимать одно число и возвращать True, если число четное, и False, если нечётное.
# Напиши функцию sum_range:
#
# Функция должна принимать два числа start и end и возвращать сумму всех чисел в этом диапазоне, включая границы.
