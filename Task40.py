# 40. Определить, присутствует ли в заданном списке строк, некоторое число 

A = input('Введите данные: ').split()
for i in range(len(A)):
    A[i] = int(A[i])
x = int(input('Введите искомое число '))
if x in A: print('Число притутствует')
else: print('Числа нет')