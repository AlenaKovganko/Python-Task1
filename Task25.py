# 25 Найти сумму чисел от 1 до А
def sum (A):
    sum = 0
    for i in range(1,A):
        sum = i + sum
    return  sum
print (sum(A = int(input('введите число А '))))
