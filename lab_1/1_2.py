# Лабораторная работа 1

# 2. Разработайте алгоритм, который запрашивает у пользователя четыре целых числа и затем находит
# третье по величине число, если оно существует. Нарисуйте блок-схему алгоритма.

array = [int(input()), int(input()), int(input()), int(input())]

num = None

for i in range(len(array)):
    h = 0
    for j in range(len(array)):
        if array[j] > array[i]:
            h += 1
        elif h == 3:
            num = j

if not num:
    print('Нет 3 по значению элемента')
else:
    print(f'Третий по величине элемент - {num}')

