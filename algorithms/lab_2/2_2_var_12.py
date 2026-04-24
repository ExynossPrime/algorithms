# Лабораторная работа 2

# 2. Вариант 12. Найти максимальный элемент массива X(10).

import random

array = []

for i in range(10):
    array.append(random.randint(1, 100))

print(array)
search_num = 0
for i in array:
    if i > search_num:
        search_num = i

print(search_num)