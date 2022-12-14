# 1. Программа принимает на вход вещественное число и показывает сумму его цифр.

num = input("Введите дробь: ")
mass = num.split('.')
a = int(mass[0])
b = int(mass[1])
sum = 0
while (a != 0):
    sum += a %10
    a = a // 10
while (b != 0):
    sum += b%10
    b = b // 10
print(int(sum))



# 2. Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("n = "))
numbers = []
a = 1
for i in range(1, n+1):
    if i == 0:
        numbers.append(1)
        continue
    a *= i
    numbers.append(a)
print(numbers)



# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input("n = "))
lst = [round((1+1/i)**i, 3)
for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')



# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

n = int(input("n = "))
lst = list(map(int, range(-n, n+1)))
print(lst)
i_str = input("индексы через пробел: ")
i_str = i_str.split()
i_int = [int(x) for x in i_str]
num = []
for i in i_int:
    j = 0    
    if i_int[j] in lst:
        num.append(lst[i])
        j += 1
print(num)
mult = 1
for i in num:
    mult *= i
print(mult)



# 5. Реализуйте алгоритм перемешивания списка.

from random import randrange
n = 5
a = [randrange(1, 10) for i in range(n)]
print("список: ")
print(a)

from random import shuffle
shuffle(a)
print("перемешанный список: ")
print(a)