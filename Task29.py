# 29 Написать программу вычисления произведения чисел от 1 до N
def multiplication(N):
    m = 1
    for i in range(1,N+1):
        m *= i
    print(m)
multiplication(N = int(input('Введите число N ')))


