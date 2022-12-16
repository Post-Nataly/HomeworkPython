# Файлы, tuple, set, dict

# 'r' - чтение
# 'w' - перезапись (если файла нет, его создадут)
# 'a' - дозапись
# 'r+' - чтение + запись

# from pathlib import Path # импортируем из библиотеки
 
# file_path = Path('data', 'text.txt')
# with open('file.txt', 'r') as f_data:  # такое написание позволяет отлавливать ошибки внутри
#     print(f_data.read())

# set - множество
# Хэш - уникальная ссылка на ячейку памяти, в которой хранится неизменяемый(!) элемент

# работа со слловарями:

# my_dict = {
#     'key_1': 12,
#     'key_2': 54,
#     'key_3': {
#         'key_4': [1, 2, 3]
#         }
#     }

# for key in my_dict:
#     print(key)

# my_dict = {
#     'key_1': 12,
#     'key_2': 54,
#     'key_3': {
#         'key_4': [1, 2, 3]
#         }
#     }

# for dbl in my_dict.items():
#     print(dbl)


# 1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл (minn maxx).

# f_path = 'test.txt'

# with open(f_path, 'r') as f_nums:
#     list_nums = f_nums.read().split(' ')
# # print(list_nums)
# for i in range(len(list_nums)):
#     list_nums[i] = int(list_nums[i])

# minmax_list = [min(list_nums), max(list_nums)]

# with open(f_path, 'a') as min_max:
#     min_max.writelines(f"\n {minmax_list} ")  # в файл test.txt добавился массив из макс. и мин. значений



# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python (scipy)

# 1)
# a = int(input('введите число a: '))
# b = int(input('введите число b: '))
# c = int(input('введите число c: '))

# discr = b * b - 4 * (a * c)

# if discr == 0:
#     my_tuple = (-b / (2 * a),)
# elif discr > 0:
#     my_tuple = ((-b + discr ** 0.5) / (2 * a), (-b - discr ** 0.5) / (2 * a))
# else:
#     my_tuple = ('фигня',)
# print(my_tuple)



# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input("Введите 1 число >> "))
b = int(input("Введите 2 число >> "))


def NOK(a,b):
    i = 2 # min(a, b)
    while True:
        if a%i==0 and b%i==0:
            break
        i += 1
        return i

print(NOK(a,b))