# 1. Программа принимает на вход вещественное число и показывает сумму его цифр.

num = input("Введите дробь: ")
mass = num.split(".")
a = int(mass[0])
b = int(mass[1])
sum = 0
while (a != 0):
    sum += a%10
    a = a // 10
while (b != 0):
    sum += b%10
    b = b //10

print(int(sum))