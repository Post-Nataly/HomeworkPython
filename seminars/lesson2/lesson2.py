# работа с файлами

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # а - добавление данных, r - чтение, w - запись
# data.writelines(colors) # для записи набора данных (без разделителей)
# data.close() # закрыть файл
# colors = ['red', 'green', 'white']
# data = open('file.txt', 'w')
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# другой вариант открытия файла:
# with open('file.txt', 'a') as data:
#     data.write('\nline 111\n')
#     data.write('line 222\n')

# path = 'file.txt'        # создали путь к папке
# data = open(path, 'r')   # открыли для чтения
# for line in data:        # проходим по файлу, считывая все строки
#     print(line)          # выводим
# data.close               # закрываем

# exit() # чтобы не читался код ниже

# импорт функции из файла

# import lesson1     # если написать import lesson1 as l, то в дальнейшем можно писать l вместо lesson1
# print(lesson1.f(1))



# функции по умолчанию

# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5))       # !!!!!

# # или

# def new_string(symbol, count = 5):
#     return symbol * count
# print(new_string('!'))       # !!!!!
# print(new_string(4))         # 20

# возможность передачи неограниченного кол-ва аргументов 

# def con(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(con('a', 's', '2')) # as2
# если передать числа без кавычек будет ошибка, т.к. это сторка!!



# # рекурсия

# # фибоначчи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)            # 1 1 2 3 5 8 13 21 34



# кортеж (неизменяемый список)

# a = (2, 4)
# print(a)                              # (2, 4)
# print(a[0])

# t = tuple(['red', 'green', 'blue'])                  # создаем список и конвертируем его в кортеж
# red, green, blue = t                                 # праспаковываем кортеж, превращая его в независимые переменные
# print('r:{} g:{} b:{}'. format(red, green, blue))    # r:red g:green b:blue



# словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}             # создали пустой словарь
# dictionary = \
#     {
#         'up': 'u',
#         'left': 'l',
#         'down': 'd',
#         'right': 'r'
#     }
# print(dictionary)           # {'up':'u', 'left':'l', 'down':'d', 'right':'r'}
# print(dictionary['left'])   # l

# for k in dictionary.keys():
#     print(k)                # up left down right
#     print(dictionary[k])      # l u l d r



# множества

# colors = {'red', 'green', 'blue'}
# print(type(colors))                   # <class 'set'>
# colors.add('red')         # аргумент не добавится, т. к. он уже есть
# colors.add('white')
# print(colors)             # {'white', 'red', 'green', 'blue'}
# colors.remove('white')    # {'red', 'green', 'blue'}
# colors.discard('white')   # удаление несуществующего элемента не вызовет ошибку
# colors.clear()            # { } пустое множество
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()              # c = {1, 2, 3, 5, 8}
# u = a.union(b)            # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)     # i = {8, 2, 5}
# dl = a.difference(b)      # dl = {1, 3}
# dr = b.difference(a)      # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))  # {1, 21, 3, 13}

# s = frozenset(a)          # замороженное множество



# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
# list1[0] = 10
# list2[1] = 15
# print(list1)
# print(list2)        # изменения происходят в обоих списках

# print(len(list1))    # 5
# print(list1.pop())   # 5
# print(list1)         # [10, 15, 3, 4]
# print(list1.pop())   # 4
# print(list1)         # [10, 15, 3]

# print(list1.insert(2, 11))
# print(list1)         # [10, 15, 11, 3]

# print(list1.append(11))
# print(list1)         # [10, 15, 11, 3, 11]