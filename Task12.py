# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3
sum_of_numbers = int(input("Введите сумму чисел: "))
product_of_numbers = int(input("Введите произведение чисел: "))


def guess_numbers(sum, product):
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i * j == product_of_numbers and i + j == sum_of_numbers:
                return f"Петя загадал числа {i} и {j}"
    return "Таких чисел в диапазоне 1-1000 не существует"


print(guess_numbers(sum_of_numbers, product_of_numbers))
