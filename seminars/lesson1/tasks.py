# 1 Программа отвечает "да", если ожно из чисел
# является квадратом другого, и "нет" в другом случае

# print('введите а')
# a = float(input())
# print('введите b')
# b = float(input())
# if a ** 2 == b:
#     print("да")
# elif b ** 2 == a:
#     print("да")
# else: 
#     print("нет")


# 2 Программа принимает на вход 5 чисел и находит максимальное

# from random import randint #если пользователь вводит число, то эта строка не нужна
numbers = []
# #numbers = [].pop() pop принимает индекс элемента, который нужно удалить
# #или remove, который принимает значение элемента
for i in range(5):
#     numbers.append(randint(-100, 100)) # 
    numbers.append(int(input('--> ')))
max_count = max(numbers)
print(numbers)
print(max_count)


# срезы массивов:
# a = [42, 67, 12, 87, 112]

# a[1:3] -> [67, 12]
# a[2:] -> [12, 87, 112]
# a[::2] -> [42, 12, 112]


# 3 Программа принимает на вход число N и выводит числа от -N до N

# print('введите чило N:')
# N = float(input())
# numbers = []
# for i in range(-N, N+1):
#     numbers.append(i)
# print(numbers)


# 4 Программа принимает на вход дробь 
# и показывает первую цифру дробной части числа

# a = float(input("Введите дробь: "))
# b = (a * 10) % 10
# print(int(b))

# или (обязательно дробь через запятую)

# string = input('введите дробь через запятую: ').split(',')[1][0]
# print(string)


# 5 Программа принимает на вход число и проверяет кратно ли оно (5 и 10)
# или (15, но не 30)

n = int(input("введите число "))
print(((n % 5 == 0) and (n % 10 == 0)) or ((n % 15 == 0) and (n % 30 != 0)))