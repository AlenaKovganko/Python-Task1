#24 Найти кубы чисел от 1 до N
def cube(N):
    for i in range(1,N):
        print (i, '-',i*i*i)
cube (N = int(input('Введите N  ')))