# 26 Возведите число А в натуральную степень B используя цикл
def degree(A,B):
    d = A
    for i in range (1,B):
        d = d * A
    return d
print (degree(A = int(input('Введите число A ')),B = int(input('Введите число B ')) ))

