# 1. Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

import math

π = math.pi
d = 0.001

d = str(d)
i = '.'
if i in d:
    a = len(d) - d.index(i) - 1
    π = round(π, a)
    print(π)
else:
    print('число d целое')



# 2. Программа составляет список простых множителей числа N.

n = int(input('Введите число n: '))
a = []
x = 2
while x * x <= n:
    if n % x == 0:
        a.append(x)
        n //= x
    else:
        x += 1
else:
    a.append(n)

print(a)



# 3. Программа выводит список неповторяющихся элементов в заданном списке.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

lst = [1, 1, 2, 3, 4, 4, 4]

numb_repit = []
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    numb_repit.append(count)

uniq = set()
index = 0
while index < len(lst):
    if numb_repit[index] == 1:
        uniq.add(lst[index])
    index += 1
        
print(list(uniq))


# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

data = open('seminars/lesson2/file.txt', 'a')

from random import randint

k = int(input(''))

coefficients = []
for i in range(k+1):
    coefficients.append(randint(0, 100))
while k > 2:
    for i in range(k-1):
        data.write(str(f"{coefficients[i]} * (x ** {k}) + "))
        k -= 1
        i += 1
else:
    data.write(str(f"{coefficients[-2]} * x + {coefficients[-1]} = 0"))

data.close()



# 5. Даны два файла, в каждом из которых находится запись многочлена.
#    Сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).
#    Пример итогового файла: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

data = open('seminars/lesson2/file.txt', 'r')

poly1 = data.readline()
print(poly1)

poly1 = poly1.split(' ')

polynom1 = list(reversed(poly1))

polynom1[2] = int(polynom1[2])

a = 0
while a < len(polynom1) + 1:
    polynom1[a] = int(polynom1[a])
    a += 6

data = open('seminars/lesson2/newfile.txt', 'r')

poly2 = data.readline()
print(poly2)

poly2 = poly2.split(' ')

polynom2 = list(reversed(poly2))

polynom2[2] = int(polynom2[2])

a = 0
while a < len(polynom2) + 1:
    polynom2[a] = int(polynom2[a])
    a += 6

polynom3 = []
if len(polynom1) > len(polynom2):
    for i in polynom1:
        polynom3.append(i)
    a = 2
    while a < len(polynom2):
        if a == 2:
            polynom3[a] = polynom1[a] + polynom2[a]
            a += 4
        if a == 6:
            polynom3[a] = polynom1[a] + polynom2[a]
            a += 6
else:
    for i in polynom2:
        polynom3.append(i)
    a = 2
    while a < len(polynom1):
        if a == 2:
            polynom3[a] = polynom1[a] + polynom2[a]
            a += 4
        if a == 6:
            polynom3[a] = polynom1[a] + polynom2[a]
            a += 6
        polynom3[a] = polynom1[a] + polynom2[a]
        a += 6

polynom3[2] = str(polynom3[2])

a = 0
while a < len(polynom3) + 1:
    polynom3[a] = str(polynom3[a])
    a += 6

pol_str = list(reversed(polynom3))

pol_end = " ".join(pol_str)
print(pol_end)

data = open('seminars/lesson2/lostfile.txt', 'a')
data.write(pol_end)
data.close() 