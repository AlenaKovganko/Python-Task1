# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
from random import randrange
n = int(input('Введите количество чисел '))
a =[randrange(1,5) for i in range(n)]
print(a)
b = []
print(b)
for i in a:
    for j in (len(b)):
        b.append(int(i))   
print(b)