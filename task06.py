# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета
# Примеры:
# 385916 -> yes
# 123456 -> no

number = int(input("Введите число: "))
digitsArray = [None] * 6

for i in range(6):
    digitsArray[5 - i] = number % 10;
    number //= 10

sumFromStart = 0
sumFromEnd = 0

for i in range(3):
    sumFromStart += digitsArray[i]
    sumFromEnd += digitsArray[5 - i]

if (sumFromEnd == sumFromStart): print("yes")
else: print("no")