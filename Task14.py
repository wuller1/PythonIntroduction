# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

def powers_of_two(end_number):
    powers_of_two_array = [1]
    current_number = 1

    while powers_of_two_array[-1] < end_number:
        if 2 ** current_number > end_number:
            break
        powers_of_two_array.append(2 ** current_number)
        current_number += 1
    return powers_of_two_array


number = int(input("Введите целое число: "))
print(powers_of_two(number))
