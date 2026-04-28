# Лабораторная работа 1

# 3. Разработайте алгоритм, который случайным образом задает четыре целых числа и затем определяет
# максимальное и минимальное число, а также находит количество максимальных и минимальных
# чисел среди введенных. Нарисуйте блок-схему алгоритма.

import random

array = []

for i in range(4):
    array.append(random.randint(1, 100))

print(array)

min = array[0]
max = array[0]
min_count = 0
max_count = 0

for i in array:
    if i < min:
        min = i
        min_count = 1
    elif i == min:
        min_count += 1

    if i > max:
        max = i
        max_count = 1
    elif i == max:
        max_count += 1

print(f'Минимальное значение {min} встречается {min_count} раз')
print(f'Максимальное значение {max} встречается {max_count} раз')


