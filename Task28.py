# 28 Подсчитать сумму цифр в числе
def sum (A):
    sum = 0
    c = 0
    while A > 0:
        sum = int(A%10) + sum
        A = int(A/10)
    print (sum)
sum (A = int(input('Введите число A ')))