# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# def f(x):
#     return x**2

# print(f(2))

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def math(op, x):   # op - функция (операция), х - число
#     print(op(x))

# math(f, 10)

# # если много похожих функций:

# def sum(x, y):
#     return x + y

# f = lambda x, y: x + y   # тоже самое что и функция sum

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))

# calc(f, 4, 5)  # можно записать calc(lambda x, y: x+y, 4, 5)



# List Comprehension

# list = []

# for i in range(1, 21):
#     if(i % 2 == 0)
#     list.append(i)

# print(list)
# тоже самое в одну строку:
# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list)

# добавим возведение в степень:

# def f(x):
#     return x**3

# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)

# # чтобы показать число и его куб, добавим кортежи:

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)



# Анонимные, lambda функции

# В файле хранятся числа, нужно выбрать четные 
# и составить список пар (число; квадрат числа)
# Пример: 1 2 3 4 5 8 --->  [(2, 4), (4, 16), (8, 64)]

# path = '/путь к файлу'
# f = open(path, 'r')   # открываем файл для чтения
# data = f.read() + ' ' # считываем строку и добавляем пробел
# f.close()             # закрываем файл

# numbers = []

# while data != '':                       # делаем проверку строки, пока она не пустая
#     space_pos = data.index(' ')         # ищем первую позицию пробела
#     numbers.append(int(data[:space_pos])) # берем все, что находится до первого пробела, превращаем в число и добавляем список чисел
#     data = data[space_pos + 1:]           # обновляем строку с учетом того, что то, что мы добавили, больше не нужно использовать

# out = []
# for e in numbers:
#     if not e % 2:                       # проверка четности
#         out.append((e, e ** 2))         # добавляем в новый список кортежи (само число, его квадрат)
# print(out)

# ------

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)                  # [1, 2, 3, 5, 8, 15, 23, 38]
# res = where(lambda x: not x % 2, res)    # [2, 8, 38]
# res = select(lambda x:(x, x**2), res)    # [(2, 4), (8, 64), (38, 1444)]
# print(res)


# Функция map (вместо функции select)

# li = [x for x in range(1, 10)]         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# li = list(map(lambda x: x + 10, li))   # [11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(li)

# --------

# data = list(map(int, input().split()))
# print(data)                                # список введенных чисел



#  Функция filter (вместо функции where)

# data = [x for x in range(10)]

# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)                                     # [0, 2, 4, 6, 8]



# Функция zip (объединяет списки)

# users = ['users1', 'users2', 'users3', 'users4', 'users5']
# ids = [4, 5, 6, 14, 7]

# data = list(zip(users, ids))
# print(data)                     # [('users1', 4), ('users2', 5), ('users3', 6), ('users4', 14), ('users5', 7)]



# Функция enumerate

# users = ['users1', 'users2', 'users3', 'users4', 'users5']

# data = list(enumerate(users))
# print(data)                       # [(0, 'users1'), (1, 'users2'), (2, 'users3'), (3, 'users4'), (4, 'users5')]