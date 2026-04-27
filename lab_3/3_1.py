# Лабораторная работа 3

# Написать единую программу на языке высокого уровня, реализующую
# сортировку массива, заполненного случайными числами в диапазоне от 0 до 100,
# различными методами. Провести сравнительный анализ временной эффективности
# реализованных методов.

# Должны быть реализованы следующие методы сортировки:

# Сортировка методом прямого обмена (сортировка методом пузырька).
# Сортировка методом прямого включения.
# Сортировка методом прямого выбора.
# Шейкерная сортировка.
# Сортировка методом Шелла.
# Сортировка методом Хоара.

import random
import time

array = []
time_sort = {}

for i in range(10):
    array.append(random.randint(1, 100))

print('Изначальный массив', array, '\n')

array_1 = array.copy()
array_2 = array.copy()
array_3 = array.copy()
array_4 = array.copy()
array_5 = array.copy()
array_6 = array.copy()

# сортировка пузырьком
print('Сортировка методом прямого обмена (сортировка методом пузырька)')
start = time.time()
h = 0
while h == 0:
    for i in range(len(array_1)):
        for j in range(len(array_1)):
            if array_1[i] < array_1[j]:
                array_1[i], array_1[j] = array_1[j], array_1[i]
            else:
                h -= 1
print(array_1)
stop = time.time()
print(f'Время работы в миллисекундах: {(stop - start) * 1000} \n')
time_sort['Сортировка методом прямого обмена (сортировка методом пузырька)'] = (stop - start) * 1000


# Сортировка методом прямого включения
print('Сортировка методом прямого включения')
start = time.time()

#код

print(array_2)
stop = time.time()
print(f'Время работы в миллисекундах: {(stop - start) * 1000} \n')
time_sort['Сортировка методом прямого включения'] = (stop - start) * 1000


# Сортировка методом прямого выбора
print('Сортировка методом прямого выбора')
start = time.time()

#код

print(array_3)
stop = time.time()
print(f'Время работы в миллисекундах: {(stop - start) * 1000} \n')
time_sort['Сортировка методом прямого выбора'] = (stop - start) * 1000


# Шейкерская сортировка
print('Шейкерская сортировка')
start = time.time()

#код

print(array_4)
stop = time.time()
print(f'Время работы в миллисекундах: {(stop - start) * 1000} \n')
time_sort['Шейкерская сортировка'] = (stop - start) * 1000


# Сортировка методом Шелла
print('Сортировка методом Шелла')
start = time.time()

#код

print(array_5)
stop = time.time()
print(f'Время работы в миллисекундах: {(stop - start) * 1000} \n')
time_sort['Сортировка методом Шелла'] = (stop - start) * 1000


# Сортировка методом Хоара
print('Сортировка методом Хоара')
start = time.time()

#код

print(array_6)
stop = time.time()
print(f'Время работы в миллисекундах: {(stop - start) * 1000} \n')
time_sort['Сортировка методом Хоара'] = (stop - start) * 1000


for i, j in time_sort.items():
    print(f'{i}: {j} миллисекунд')
