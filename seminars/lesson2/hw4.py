# 1. Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

# import math

# π = math.pi
# d = 0.001

# d = str(d)
# i = '.'
# if i in d:
#     a = len(d) - d.index(i) - 1
#     π = round(π, a)
#     print(π)
# else:
#     print('число d целое')



# 2. Программа составляет список простых множителей числа N.

# n = int(input('Введите число n: '))
# a = []
# x = 2
# while x * x <= n:
#     if n % x == 0:
#         a.append(x)
#         n //= x
#     else:
#         x += 1
# else:
#     a.append(n)

# print(a)



# 3. Программа выводит список неповторяющихся элементов в заданном списке.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# lst = [1, 1, 2, 3, 4, 4, 4]

# numb_repit = []
# for i in lst:
#     count = 0
#     for j in lst:
#         if i == j:
#             count += 1
#     numb_repit.append(count)

# uniq = set()
# index = 0
# while index < len(lst):
#     if numb_repit[index] == 1:
#         uniq.add(lst[index])
#     index += 1
        
# print(list(uniq))


# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

# data = open('seminars/lesson2/newfile.txt', 'a')

# from random import randint

# k = int(input(''))

# coefficients = []
# for i in range(k+1):
#     coefficients.append(randint(0, 100))
# while k > 2:
#     for i in range(k-1):
#         data.write(str(f"{coefficients[i]} * (x ** {k}) + "))
#         k -= 1
#         i += 1
# else:
#     data.write(str(f"{coefficients[-2]} * x + {coefficients[-1]} = 0"))



# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0