""" 
Задайте последовательность чисел. 
Напишите программу, которая выведет 
список неповторяющихся элементов 
исходной последовательности. 
"""
import random

numl = [random.randint(0, 20) for i in range(0, 20)]
print("\nИсходная последовательность чисел:")
numl2 = numl[:]
print(numl)
numl = set(numl)
lis = []
for numls in numl:
    lis.append(numls)
print("\nНЕповторяющиеся элементы исходной последовательности:")
print(lis, end='\n\n')
