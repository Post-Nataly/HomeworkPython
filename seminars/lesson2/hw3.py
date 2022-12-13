# 1. Программа находит сумму элементов списка, стоящих на нечётных идексах.

# from random import randrange
# a = [randrange(1, 10) for i in range(6)]
# print("список: ")
# print(a)
# s = 0
# for i in range(len(a)):
#     if (i % 2 != 0):
#         s += a[i]
# print("сумма элементов на нечетных индексах:")
# print(s)



# 2. Программа найдёт произведение пар чисел списка. 
#    Пара - первый и последний элемент, второй и предпоследний и т.д.

# from random import randrange
# a = [randrange(1, 10) for i in range(7)]
# print("список: ")
# print(a)
# b = []
# m = 0
# j = 0
# for i in range(len(a)):
#     if j + i < len(a):
#         m = a[i] * a[len(a)-1-j]
#         b.append(m)
#         j += 1
# print("список пар:")
# print(b)


# 3. Программа ищет разницу между максимальным и минимальным значением дробной части элементов списка из вещественных чисел.

# - [1.1, 1.2, 3.1, 10.01] => 0.19

# import random
# a = [float(random.random()*10) for i in range(7)]
# b = []
# for i in a:
#     b.append('%.2f' % i)
# b = [float(x) for x in b]
# print("список: ")
# print(b)
# c = []
# for i in b:
#     i *= 100
#     i = i % 100
#     c.append(int(i))
# print('%.2f' % (max(c)/100 - min(c)/100))



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = 1
# def binary(n):
#     while n > 0:
#         if (n % 2 == 0):
#             return 0
#         else:
#             return 1
#     n = round(n / 2)
# c = []
# for i in c:
#     c.append(binary(a))
# print(*c)
# print(binary(a))



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [1, 2]:
        return 1
    elif (n < 0)
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(0, 10):
    list.append(fib(e))
print(list)