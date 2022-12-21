# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

import re


# print(eval(input("Введите вычмсляемое выражение: ")))


def parse_symbols(full_string):
    res_list = []
    for i in full_string:
        if i in "+-/*":
            res_list.append(i)
            return res_list


# def calc(num_list: list, op_list: list):
# while len(num_list) > 1:
# if ('*' in op_list) and ('/' in op_list):
# if op_list.index('*') < op_list.index('/'):
# i = op_list.index('*')
# sc = '*'
# else:
# i = op_list.index('/')
# sc = '/'
# elif '*' in op_list:
# i = op_list.index('*')
# sc = '*'
# elif '/' in op_list:
# i = op_list.index('/')
# sc = '/'
# elif ('+' in op_list) and ('-' in op_list):
#
#
# tmp = list(num_list[i] * num_list[i + 1])
# num_list = num_list[:i] + tmp + num_list[i + 2:]
# op_list.remove(sc)
#
# expression = input("Введите вычисляемое выражение: ")

expression = "23+54-47*895/1452+65"
symbs = parse_symbols(expression)
expression = (re.findall(r'-|/|\+|\*|[\d]+', expression))
print(expression)
print(symbs)


# 2
def Summ (num1, num2):
    return num1 + num2
def Minus (num1, num2):
    return num1 - num2
def Multiplication (num1, num2):
    return num1 * num2
def Division (num1, num2):
    return num1/num2


user_string = '1-3*6'

def user_do (user_string ):
    res = ' '
    for i in range (0, len(user_string)):
        if (user_string[i] == '*') or (user_string[i] =='/'):
            if user_string[i] == '*':
                temp_value = str(Multiplication(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
                print(res)
                return res
            if user_string[i] == '/':
                temp_value = str(Division(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
            print(res)
        return res
    for i in range (0, len(user_string)):
        if (user_string[i] == '+') or (user_string[i] =='-'):
            if user_string[i] == '+':
                temp_value = str(Summ(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
                print(res)
                return res
            if user_string[i] == '-':
                temp_value = str(Minus(int(user_string[i-1]),int(user_string[i+1])))
                res = user_string[:i-1] + temp_value + user_string[i+2:]
                print(res)
            return res




user_do(user_string)

user_do(user_do(user_string))