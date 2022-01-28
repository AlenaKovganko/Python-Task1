# 8. Показать четные числа от 1 до N
N = int(input('Enter the number:'))

for i in range (1, N):
    if i % 2 == 0:
        print (i)
