# 46 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
def fib(n):
    if n in [1,2]: return 1
    if n > 0: return fib(n-1) + fib (n-2)
    if n < 0: return (fib(n+2) - fib (n+1))
        
def fib2(N1, N2):
    fibon = []
    for i in range (N1, N2):
        fibon.append(fib(i))
    return fibon

print(fib2(N1 = int(input('Введите начальное число')),N2 = int(input('Введите конечное число'))))

