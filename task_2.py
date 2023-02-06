""" 
Задайте натуральное число N. 
Напишите программу, 
которая составит список простых множителей числа N. 
78 = 2*3*13
"""
import random

n = random.randint(2, 1000)
t = n
st = ''
flag = False
for i in range(2, t):
    for j in range(2, n):
        if t % i == 0:
            t /= i
            st += str(i) + '*'
            flag = True

if flag:
    print(f"\nCписок простых множителей числа {n} = {st[:-1]}\n")
else:
    print(f"\nЧисло {n} = простое\n")
