#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень 
# B с помощью рекурсии.
#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8

def power (a, n):
    if n == 0:
        return 1
    else:
        return power(a, n - 1)*a

a = int(input('введите число А = '))
b = int(input('введите число В = '))
res = power(a, b)
print(res)
