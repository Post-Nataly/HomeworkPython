# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел (time).

from datetime import datetime

# def numbers(a):
#     now = datetime.now()
#     number = now.time().second ** now.time().minute * now.time().microsecond // now.time().minute # арифметические действия с текущим временем
#     return number % 10**a

# print(numbers(3)) 



# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# def find_i(sp: list, word: str) -> int:
#     if word not in sp:
#         return -1
#     n1 = sp.index(word)
#     return sp.index(word, n1 + 1) if word in sp[n1 + 1:] else -1

# lst = ['фыв', 'йцу', 'ячс', 'цук', 'йцу', 'йцукен']
# print(find_i(lst, 'йцу'))

# или

def find_i(list: list, num):
    count = 0
    for i in range(len(list)):
        if num == list[i]:
            count +=1
        if count == 2:
            return i
    return -1

lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num = input("Write string: ")

print(find_i(lst, num))