# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2
def count_in_array(value, array):
    count = 0
    for item in array:
        if item == value:
            count += 1
    return count


def minimum(number1, number2):
    return number2 if number1 > number2 else number1


coins = input("Введите расположение монеток через пробел: 1 - орел, 0 - решка: ").split(" ")
print(coins)
headsCount = count_in_array("1", coins)
tailsCount = count_in_array("0", coins)
minNumber = minimum(headsCount, tailsCount)
print(minNumber)
