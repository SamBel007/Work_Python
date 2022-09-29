#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно чи5сло квадратом другого.
#*Примеры:*
#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет

print('write first number(a):')
a = int(input())
print('write second number(b):')
b = int(input())


if a ** 2 == b or b ** 2 == a:
    print ("Answer : " , '-> yes <-')
else:
    print ("Answer : " ,'-> no <-')   