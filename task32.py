# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)

minNumber = int(input("Введите минимальное значение: "))
maxNumber = int(input("Введите максимальное значение: "))

listOfElements = [0, 2, 10, 20, 3, 29, 100, 40, 18, -10, -32, 24]
indices = []

for i in range(0, len(listOfElements)):
    if minNumber <= listOfElements[i] <= maxNumber:
        indices.append(i)

print(indices)
