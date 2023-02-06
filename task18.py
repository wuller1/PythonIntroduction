# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

import random

def closestElementInArray(value, array):
    closestIndex = 0;
    for index, number in enumerate(array):
        if abs(number - value) < abs(array[closestIndex] - value):
            closestIndex = index;
    return array[closestIndex]

def generateRandomArray(N):
    array = [0] * N
    for i in range(0, len(array)):
        array[i] = random.randint(1, 10)
    return array

N = int(input("Введите размер массива: "))
number = int(input("Введите число: "))
randomArray = generateRandomArray(N)
closestElement = closestElementInArray(number, randomArray)

print(f"В заданном массиве {randomArray} самый близкий по величине элемент - {closestElement}")