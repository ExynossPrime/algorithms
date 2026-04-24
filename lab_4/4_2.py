# Лабораторная работа 4

# 2. Написать программу на языке высокого уровня, реализующую
# поиск подстроки в строке.

import random
import string

characters = string.ascii_lowercase
string = ''.join(random.choices(characters, k=30))

print(string)

search_string = str(input())

for i in range(len(string) - len(search_string) + 1):
    for j in range(len(search_string)):
        p = True
        if search_string[j] != string[i + j]:
            p = False
            break
    if p:
        print(f'Подстрока {search_string} начинается с {i} элемента')
    else:
        print('Подстрока не найдена')

