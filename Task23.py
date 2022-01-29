# 23 Показать таблицу квадратов чисел от 1 до N
def square(N):
    for i in range(1,N):
        print (i, '-',i*i)
square (N = int(input('Введите N  ')))
