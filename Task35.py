# 35 Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогдаn[ 1, 2, 6, 24 ]
n = int(input('Введите n '))
m = 1
List_m = []
for i in range(1, n+1):
    m *= i
    List_m.append(m)

print(List_m)
