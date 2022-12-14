# 1. Программа находит сумму элементов списка, стоящих на нечётных идексах.

from random import randrange

a = [randrange(1, 10) for i in range(6)]
print("список: ")
print(a)

s = 0
for i in range(len(a)):
    if (i % 2 != 0):
        s += a[i]

print("сумма элементов на нечетных индексах:")
print(s)



# 2. Программа найдёт произведение пар чисел списка. 
#    Пара - первый и последний элемент, второй и предпоследний и т.д.

from random import randrange

a = [randrange(1, 10) for i in range(11)]
print("список: ")
print(a)

b = []
m = 0
j = 0
for i in range(len(a)):
    if j + i < len(a):
        m = a[i] * a[len(a)-1-j]
        b.append(m)
        j += 1

print("произведения пар:")
print(b)


# 3. Программа ищет разницу между максимальным и минимальным значением дробной части элементов списка из вещественных чисел.

# - [1.1, 1.2, 3.1, 10.01] => 0.19

import random

a = [float(random.random()*10) for i in range(7)]
b = []
for i in a:
    b.append('%.2f' % i)
b = [float(x) for x in b]
print("список: ")
print(b)

c = []
for i in b:
    i *= 100
    i = i % 100
    c.append(int(i))
print('%.2f' % (max(c)/100 - min(c)/100))



# 4. Программа преобразовывает десятичное число в двоичное.

a = int(input('Введите число: '))

b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2
  
print(b)



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
        
k = int(input('Введите число: '))

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list1 = []
for e in range(1, k+1):
    list1.append(fib(e))

list2 = list1[::-1]
for e in range(1, k+1):
    if (len(list2) / 2 != 0):
        if e%2 != 0:
            list2[e-1] = list2[e-1]*(-1)
        else:
            continue

list3 = list2 + list1
list3[k:k:1] = [0]

print(list3)