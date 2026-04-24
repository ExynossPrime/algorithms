# Лабораторная работа 2

# 3. Вариант 12. Дан массив X(14). Заменить все элементы массива, значения которых меньше 2, нулями.

import random

array = []

for i in range(14):
    array.append(random.randint(1, 10))

print(array)

for i in range(len(array)):
    if array[i] < 2:
        array[i] = 0

print(array)