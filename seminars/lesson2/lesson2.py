# вывод строки
s = 'hello, World!'
print(s)
a = 123
b = 1.23
print(a, '-', b, '-', s)
print('{} + {} - {}'.format(a, b, s))
print('{2} + {1} - {0}'.format(a, b, s))
print(f'{a} + {b} - {s}')

# списки (массивов как таковых в python нет)
list = ['1', '2', 'hello', True]

# ввод, вывод данных
print('введите a:')
a = int(input()) # введено целое число, b = input() - введена строка!
print('введите b:')
b = int(input())

# арифметические операции
# +, -, *  - плюс, минус, умножить
# % - остаток от деления
# / - деление для вещественных чисел
# // - деление для целых чисел
# ** - возведение в степень
c = a / b
с = round(a * b, 3) # количество знаков после запятой у дробей
print(c)

# логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in