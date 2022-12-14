# Файлы, tuple, set, dict

# 'r' - чтение
# 'w' - перезапись (если файла нет, его создадут)
# 'a' - дозапись
# 'r+' - чтение + запись

with open('text.txt', 'r') as f_data:
    print(f_data.read())