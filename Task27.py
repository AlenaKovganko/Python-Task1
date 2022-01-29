# 27 Определить количество цифр в числе
def count (A):
    c = 0
    while A > 0:
        A = A // 10
        c +=1
    print (c)
count(A = int(input('Введите число A ')))