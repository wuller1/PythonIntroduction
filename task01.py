# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
n = int(input("Введите сколько километров машина проезжает за день"))
m = int(input("Введите длину маршрута в километрах"))
print(f"Машина проедет {m} км за {(m // n) + (m % n != 0)} дней")