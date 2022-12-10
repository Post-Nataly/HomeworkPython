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

import lesson1
print(lesson1.f(1))
