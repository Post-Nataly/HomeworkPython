# вывод строки
# s = 'hello, World!'
# print(s)
# a = 123
# b = 1.23
# print(a, '-', b, '-', s)
# print('{} + {} - {}'.format(a, b, s))
# print('{2} + {1} - {0}'.format(a, b, s))
# print(f'{a} + {b} - {s}')

# списки (массивов как таковых в python нет)
# list = ['1', '2', 'hello', True]

# ввод, вывод данных
# print('введите a:')
# a = int(input()) # введено целое число, b = input() - введена строка!
# print('введите b:')
# b = int(input())

# арифметические операции
# +, -, *  - плюс, минус, умножить
# % - остаток от деления
# / - деление для вещественных чисел
# // - деление для целых чисел
# ** - возведение в степень
# c = a / b
# с = round(a * b, 3) # количество знаков после запятой у дробей
# print(c)

# логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 3 < 5 < 9
# print(a )  # true

# f = 1 > 2 or 4 < 6
# print(f)  # true

# n = [1, 2, 3, 4]
# print(not 2 in n)  # false

# is_odd = n[0] % 2 == 0
# print(is_odd ) # false

# управляющие конструкции if, if-else, while, for

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# original = 235
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Хватит')
# print(inverted) # 532 (инверсия числа)

# list = [1, 2, 3, 10, 5]
# for i in list:
#     print(i**2) # квадраты всех элементов

# list = range(10) # объект из элементов от 1 до 9 вкл-но
# for i in list:
#     print(i) # элементы от 0 до 9

# list = range(2, 5) # объект из элементов от 2 до 4 вкл-но
# for i in list:
#     print(i) # 2, 3, 4

# list = range(1, 20, 4) # объект из каждого 4-го элемента от 1 до 20
# for i in list:
#     print(i) # 1, 5, 9, 13, 17


# строки

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))        # 39
# print('ещё' in text)    # True
# print(text.isdigit())   # False
# print(text.islower())   # True
# help(text.istitle)   # в консоль выведет справку о данном методе

# срезы

# print(text[0])           # c
# # print(text[len(text)])   # IndexError
# print(text[len(text)-2]) # к
# print(text[-5])          # б
# print(text[:])           # весь текст
# print(text[2:5])         # ешь
# print(text[6:-18])       # ещё этих мягких
# print(text[0:len(text):6])# тоже что print(text[::]6) - сеикакл (каждая 6-я буква, включая 1-ю)

# списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)             # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(ran)                 # range(1, 6)
# print(type(ran))           # <class 'range'>
# numbers = list(ran)        # приведение типа range к типу list
# print(type(numbers))       # <class 'list'>

# numbers[0] = 10
# print(f'{len(numbers)} len') # 5 len (длина списка - кол-во элементов)
# print(numbers)             # [10, 2, 3, 4, 5] первому элементу присвоено другое значение

# for e in numbers:
#     print(e)                # 10, 2, 3, 4, 5

# for e in numbers:
#     print(e*2)              # 20, 4, 6, 8, 10

# numbers.append(6)           # добавить в конец
# print(numbers)              # [10, 2, 3, 4, 5, 6]
# numbers.remove(2)           # или del numbers[1]  ==  [10, 3, 4, 5, 6] 


# функции

def f(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))          # целое
print(type(f(arg)))    # <class 'str'>