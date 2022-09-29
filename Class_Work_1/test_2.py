#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

print("Write a number :")
list = []
for i in range ( 1, 6):
       list.append(int(input()))
      
max = list[0]

for i in list:
       if i > max:
          max = i
print(max)