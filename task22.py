# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

def intersection(array1, array2):

    intersectionArray = [];

    for number1 in array1:
        for number2 in array2:
            if number1 == number2:
                intersectionArray.append(number2)
    intersectionArray.sort()

    return intersectionArray

def generateRandomArray(N, min, max):
    array = [0] * N
    for i in range(0, len(array)):
        array[i] = random.randint(min, max)
    return array

numberOfItems1 = int(input("Введите количество элементов первого массива: "))
numberOfItems2 = int(input("Введите количество элементов второго массива: "))
array1 = generateRandomArray(numberOfItems1, 0, 20)
array2 = generateRandomArray(numberOfItems2, 10, 30)
print(array1)
print(array2)
print(intersection(array1, array2))