# PowerShell 7.4.1
#
#    A new PowerShell stable release is available: v7.4.4
#    Upgrade now, or check out the release page at:
#      https://aka.ms/PowerShell-Release?tag=v7.4.4
#
# PS C:\Users\A_Zadororzhnii> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> exit()
# PS C:\Users\A_Zadororzhnii> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> ^Z
#
# PS C:\Users\A_Zadororzhnii> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> ^Z
#
# PS C:\Users\A_Zadororzhnii> python
# Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 2+3
# 5
# >>> 4*5
# 20
# >>> 5-1
# 4
# >>> 40/2
# 20.0
# >>> 2**3
# 8
# >>> "hello " + " world"
# 'hello  world'
# >>> "hello" *3
# 'hellohellohello'
# >>> "hello "*3
# 'hello hello hello '
# >>> "mother\' day"
# "mother' day"
# >>> "andrii".upper()
# 'ANDRII'
# >>> len("andrii")
# 6
# >>> len(304023)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: object of type 'int' has no len()
# >>> len(str(304023))
# 6
# >>> a =4
# >>> b = 6
# >>> a*b
# 24
# >>> name = "maria"
# >>> name
# 'maria'
# >>> print(name)
# maria


# Lists
print('--------Lists---------')
# Тебе нужна упорядоченная последовательность элементов? Список — наш выбор.

# >>> []
# []
lottery = [3, 42, 12, 19, 30, 59]
print(len(lottery))
lottery.sort()  # Эта команда не возвращает ничего, она просто меняет порядок номеров в списке.
print(lottery)  # номера в списке теперь отсортированы от меньшего к большему.
# [3, 12, 19, 30, 42, 59]

lottery.reverse()  # обратили список
print(lottery)
# [59, 42, 30, 19, 12, 3]

lottery.append(199)  # добавить что-то к своему списку
print(lottery)
# [59, 42, 30, 19, 12, 3, 199]

lottery.pop(0)  # удалить что-либо из списка
print(lottery)
# [42, 30, 19, 12, 3, 199]

# Vocabularies
print('--------Vocabularies---------')
# Тебе нужны сочетания ключ/значение, чтобы быстро искать значения (по ключу) в дальнейшем? Словарь отлично подойдет.

{}  # Empty Vocabularies

participant = {'name': 'Andrii', 'country': 'World', 'favorite_numbers': [7, 42, 92]}
# Выводим значение
print(participant['name'])
print(participant['country'])
print(participant['favorite_numbers'])

# добавить новые пары ключ/значение в словарь следующим образом:
participant['favorite_language'] = 'Python'
print(participant['favorite_language'])
print(len(participant))
print(participant)

# заменить значение
participant['country'] = 'Germany'
print(participant)

# Сравнения
print('--------Сравнения---------')
# x > y означает: x больше y
# x < y означает: x меньше y
# x <= y означает: x меньше или равен y
# x >= y означает: x больше или равен y

print(5 > 2)
print(3 < 1)
print(5 > 2 * 2)
print(1 == 1)
print(5 != 1)
print(6 >= 12 / 2)
print(3 <= 2)
print('-----------------')
# and — если ты используешь оператор and, оба сравнения по обе стороны от него должны быть True (верны), чтобы результат всей команды был равен True.
# or — если ты используешь оператор or, достаточно одному из сравнений по обе стороны от него быть равным True, чтобы результат всей команды также равнялся True.

print(6 > 2 and 2 < 3)
print(3 > 2 and 2 < 1)
print(3 > 2 or 2 < 1)

# Логические значения

# Существует только два логических объекта в Python:
# •	True (Истина),
# •	False (Ложь).
print('--------Логические значения---------')
a = 2 > 5
print(a)

print(True and True)  # True
print(False and True)  # False
print(True or 1 == 1)  # True
print(1 != 2)  # True

# If...elif...else
print('--------If...elif...else---------')
# условныe операторы, которые позволяют выполнять код только при определенных условиях;

if 3 > 2:
    print('Its work!!')

# если условие не True

# Python имеет операторы elif и else:

if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

name = 'Sonja'

if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

# Можно использовать сколько угодно elif после первого if.

volume = 57

if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

# Functions

print('--------Functions---------')


def hi():
    print('Hi there!')
    print('How are you?')


hi()


# Давай напишем нашу первую функцию с параметрами. Мы будем использовать предыдущий пример — функцию, которая пишет 'hi' и имя пользователя:

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')


hi("Ola")
hi("Sonja")


def hi(name):
    print('Hi ' + name + '!')


hi("Rachel")

# Loops - Цицлы

print('--------Loops---------')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']


def hi(name):
    print('Hi ' + name + '!')


for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)
