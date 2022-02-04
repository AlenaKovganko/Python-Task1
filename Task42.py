# 42 Найти сумму чисел списка стоящих на нечетной позиции

from random import randrange
n = int(input('Введите количество чисел списка '))
a = [randrange(1, 10) for i in range(n)]
print('Рандомный список')
print(a)

sum = 0
for i in range(len(a)):
    if i%2 !=0:
        sum += a[i]
print(f'Сумма чисел, стоящих в списке на нечетной позиции {sum}')

