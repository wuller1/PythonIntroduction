# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

# 2 2
# 4

def sumOfNumbers(a, b):
    if (b == 0):
        return a
    
    a += 1
    b -= 1

    return sumOfNumbers(a, b)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
sum = sumOfNumbers(number1, number2)
print(f"{number1} + {number2} = {sum}")
