# Лабораторная работа 2

# 5. Вариант 12. Из массивов X(10) и Y(15) построить матрицу A(5,5) таким образом, чтобы
# элементы массива X были расположены выше побочной диагонали.

import random

array = [[None,None,None,None,None],
         [None,None,None,None,None],
         [None,None,None,None,None],
         [None,None,None,None,None],
         [None,None,None,None,None],]
X = []
Y = []

for i in range(10):
    X.append(random.randint(1, 10))
for i in range(15):
    Y.append(random.randint(1, 10))

print(X, Y)

var = 4

for i in range(5):
    var -= 1
    for j in range(5):
        if j <= var:
            array[i][j] = X[0]
            X.pop(0)
        else:
            array[i][j] = Y[0]
            Y.pop(0)

for i in array:
   print(' '.join(map(str, i)))

