# 1. Программа принимает на вход вещественное число и показывает сумму его цифр.

# num = input("Введите дробь: ")
# mass = num.split('.')
# a = int(mass[0])
# b = int(mass[1])
# sum = 0
# while (a != 0):
#     sum += a %10
#     a = a // 10
# while (b != 0):
#     sum += b%10
#     b = b // 10
# print(int(sum))



# 2. Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.


# n = int(input("n = "))
# numbers = []
# a = 1
# for i in range(1, n+1):
#     if i == 0:
#         numbers.append(1)
#         continue
#     a *= i
#     numbers.append(a)
# print(numbers)



# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# 
# n = int(input("n = "))
# lst = [round((1+1/i)**i, 3)
# for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

n = int(input("n = "))
lst = list(map(int, range(-n, n+1)))
print(lst)
indexes = input("индексы через пробел: ")
indexes = indexes.split()
# indexes = ''.join(indexes)
print(indexes)
# rez = 1
# for i in ind:
#     rez = int(ind[i])
#     rez *= rez
# a = ind[0]
# b = ind[1]
# print(rez)