# 1. программа принимает на вход число n и выдает последовательность из N членов.

# n = int(input("Введите n: "))

# for el in range(0, n):
#     print((-3)**el, end=', ')

# 2. Для натурального n создать словарь индекс-значение,
#  состоящий из элементов последовательности 3n + 1.
# пример:
#  для n = 6: 4, 7, 10, 13, 16, 19

# n = int(input("Введите n: "))
# numbers = list()

# for el in range(1, n + 1):
#     numbers.append(3*el + 1)

#     print(numbers)

# 3. Пользователь задает две строки, а программа определяет
#  количество вхождений одной строки в другую.
# пример: "Я люблю Python"  -> "лю"  -> 2

# a = str(input("Введите строку: "))
# b = str(input("Введите часть первой строки: "))
# print(a.count(b))
# или
# s1 = 'Я люблю люблюлюблюPython'
# s2 = 'лю'
# res = s1.split(s2)
# print(res)
# print(len(res) - 1)