# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstElement = int(input("Введите первый элемент: "))
numberOfElements = int(input("Введите количество элементов: "))
d = int(input("Введите разность: "))
progressionElements = [0] * numberOfElements

for i in range(0, numberOfElements):
    progressionElements[i] = firstElement + i * d

print(progressionElements)
