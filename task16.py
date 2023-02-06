# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1
import random

def countOccurrancesInArray(value, array):
    count = 0
    for num in array:
        if num == value:
            count += 1
    return count

def generateRandomArray(N):
    array = [0] * N
    for i in range(0, len(array)):
        array[i] = random.randint(1, 10)
    return array

N = int(input("Введите размер массива: "))
number = int(input("Введите искомое число: "))
randomArray = generateRandomArray(N)
numberOfOccurrances = countOccurrancesInArray(number, randomArray)

print(f"Число {number} встречается в массиве {randomArray} {numberOfOccurrances} раз(а)")