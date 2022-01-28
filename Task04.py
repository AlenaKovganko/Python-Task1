a = int(input('Введите число a '))
b = int(input('Введите число b '))
c = int(input('Введите число c '))
if a < b < c:
    print('c Максимальное число')
elif a < c < b:
    print('b Максимальное число')

else:
    print('a Максимальное число')