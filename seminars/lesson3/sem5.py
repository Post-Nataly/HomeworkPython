# numbs = [20, 50, 15]
# res = [item for item in numbs if item > 30]   # если = tuple и круглые скобки, то будет кортеж
#   <что сделать><с чем сделать><при каком условии>
# print(res)      # 50
# 
# Задачи:
# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнилось условие
# A[i] - 1 = A[i-1]. Найдите это число.



# 2. Дан список чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.

# Пример:  [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# li = [1, 5, 2, 3, 4, 6, 1, 7]
# my_li = [li[0]]

# for i in range(1, len(li)):
#     if my_li[-1] < li[i]:
#         my_li.append(li[i])
# print(my_li)

# та же функция одной строкой:

# [my_li.append(li[i]) for i in range(1, len(li)) if my_li[-1] < li[i]]
# print(my_li)



# 3. Напишите программу, удаляющую из текста все слова, содержащиие "абв".
# Пример: 'Я люблю абвЖвау иабв Питон'  =>  'Я люблю Питон'

# str = 'Я люблю абвЖвау иабв Питон'

# my_li = str.split()
# print(my_li)

# my_li = list(filter(lambda el: not "абв" in el, my_li))
# print(my_li)

# str = ' '.join(my_li)
# print(str)