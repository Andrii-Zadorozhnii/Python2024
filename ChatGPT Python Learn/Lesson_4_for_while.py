# Урок 4: Циклы (for и while)
# Циклы позволяют выполнять один и тот же блок кода многократно, пока выполняется определенное условие или пока не будут пройдены все элементы в коллекции.
#
# Цикл for
# Цикл for чаще всего используется для перебора элементов в коллекции (список, строка, диапазон и т.д.).

# Пример с циклом for
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Функция range(): используется для создания последовательности чисел.

# Вывод чисел от 0 до 4
for i in range(5):
    print(i)


# Цикл while
# Цикл while выполняется до тех пор, пока выполняется заданное условие. Он особенно полезен, когда заранее неизвестно количество повторений.

# Пример с циклом while
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Домашнее задание

# Используй цикл for, чтобы вывести все числа от 1 до 10.
number_list = [1,2,3,4,5,6,7,8,9,10]

for number in number_list:
    print(number)

for i in range(11):
    print(i)

for i in range(1, 11):
    print(i)

# Напиши программу, которая находит сумму всех чисел от 1 до 50 с помощью цикла for.
number_sum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
result = 0
for number in number_sum:
    result = result + number
print("final sum is: ", result)

# Additional calculation
print("final sum is: ", sum(number_sum))

result = 0
for number in range(1, 51):
    result += number
print("Final sum is:", result)


# Используй цикл while для вывода всех чисел от 10 до 1 в обратном порядке.

count = 10
while count > 0:
    print(count)
    count -= 1


# Напиши программу, которая запрашивает у пользователя ввод числа и находит его факториал с помощью цикла while.

user_input = int(input("Please write a number for calculation: "))

if user_input == 0:
    result = 1
else:
    result = 1
    while user_input > 0:
        result *= user_input
        user_input -= 1

print("Factorial number is:", result)







