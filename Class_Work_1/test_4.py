# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#*Примеры:*
#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3
print('Write a number :')
num = float(input())
f_num = int(num*10 % 10)

if num % 1 == 0:
    print("нет")
else:
    print(f_num)  