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