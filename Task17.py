# 17. По двум заданным числам проверять является ли одно квадратом другого
def squareNumber(a,b):
    if a == b*b: print (a, 'является квадратом', b)
    elif b == a*a: print (b, 'является квадратом', a)
    else: print('Не является')
squareNumber(a = int(input('Введите первое число  ')), b = int(input('Введите второе число  ')))
