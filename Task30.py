#30 Показать кубы чисел, заканчивающихся на четную циф
def cube(N):
    for i in range(1,N+1):
        if (i*i*i)%2 == 0: print (i, '-',i*i*i)
cube (N = int(input('Введите N  ')))