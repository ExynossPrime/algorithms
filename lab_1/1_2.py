# Лабораторная работа 1

# 2. Разработайте алгоритм, который запрашивает у пользователя четыре целых числа и затем находит
# третье по величине число, если оно существует. Нарисуйте блок-схему алгоритма.

# ДОДЕЛАТЬ!!!!

array = [int(input()), int(input()), int(input()), int(input())]

# h = 0
#
# while h == 0:
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#             else:
#                 h -= 1



for i in range(len(array)):
    h = 0
    num = array[i]
    for j in range(len(array)):
        if array[j] < array[i]:
            i = j
            num = array[j]
        elif array[j] > num:
            break
        else:
            h += 1
        if h == 3:
            print('Третий по величине элемент =', array[j])


    print (array[i], h)



print(array)

