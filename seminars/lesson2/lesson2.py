# работа с файлами
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # а - добавление данных, r - чтение, w - запись
data.writelines(colors) # для записи набора данных (без разделителей)
data.close() # закрыть файл