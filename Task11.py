# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
def MaxNumber (a):
    if round(a/10) > round(a%10): print (a/10)
    elif round(a/10) < round(a%10): print (a%10)
    else: print ('Цифры равны')

MaxNumber (a = int(input('Введите число от 10 до 100  ')))
