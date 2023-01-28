# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))

thirdNumber = number % 10
number //= 10
secondNumber = number % 10
number //= 10
firstNumber = number
sumOfDigits = firstNumber + secondNumber + thirdNumber

print(sumOfDigits)
 