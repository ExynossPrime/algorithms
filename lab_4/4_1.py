# Лабораторная работа 4

# 1. Написать программу на языке высокого уровня, реализующую
# поиск заданного элемента в неупорядоченном массиве.

import random

array = []

for i in range(20):
    array.append(random.randint(1, 100))

print(array)

search_num = int(input())

result = []
h = 0
for i in range(len(array)):
    if array[i] == search_num:
        result.append(i)
        h += 1

if not result:
    print('Нет искомого значения')
else:
    print(f'Число {search_num} встречается в массиве {h} раз на местах {result}')



