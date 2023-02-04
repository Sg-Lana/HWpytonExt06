#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#5
#15
#Вывод:  [1, 9, 13, 14, 19]

import random

mas=[random.randint(-10, 10) for i in range(random.randint(5,10))] #создали список случайных элементов

print(*mas) #вывели на экран

maxi=int(input("MAX= ")) # просим пользователя задать  максимум

mini=int(input("MIN= ")) # просим пользователя задать минимум

masi=[] #определяем массив, который будет формироваться

if maxi>=mini:

   for i in range(len(mas)): #идем по длине заданного массива

      if maxi>=mas[i] and mini<=mas[i]:

          masi.append(i)

   print("Кол-во:",len(masi))

   print("Индексы:",masi)