import numpy as np


task1 = np.arange(1000000)
task2 = np.random.randint(1,10,1000000)

print("Задание 1:\nВычислить сумму ряда от 0 до 999999\nОтвет: ", task1.sum())

print()

print("Задание 2:\nСреднее арифметическое этого ряда\nОтвет: ", task1.mean())

print()

print("Задание 3:\nМедиана случайных 1000000 чисел\nОтвет: ", np.median(task2))

print()

print("Задание 4:\nПроизведение случайных 1000000 чисел\nОтвет: ", np.prod(task2))

