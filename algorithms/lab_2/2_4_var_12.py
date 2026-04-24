# Лабораторная работа 2

# 4. Вариант 12. В матрице Z(6,6) найти максимальный элемент, расположенный на главной
# диагонали, и произведение всех отрицательных элементов матрицы.

import random

array = []
var_array = []

for i in range(6):
    for j in range(6):
        var_array.append(random.randint(-10, 10))
    array.append(var_array)
    var_array = []

for i in array:
   print(' '.join(map(str, i)))

search_num = array[0][0]
product_negative = 1

for i in range(6):
    for j in range(6):
        if i == j and array[i][j] > search_num:
            search_num = array[i][j]
        if array[i][j] < 0:
            product_negative *= array[i][j]

print(f'Максимальный элемент главной диагонали матрицы равен {search_num}')
print(f'Произведение всех отрицательных элементов матрицы равно {product_negative}')
