# 15. Дано число. Проверить кратно ли оно 7 и 23
def multiplicity(a):
    if a%7==0 and a%23==0: print('Число кратно')
    else: print('Число некратно')

multiplicity(a = int (input('Введите число ')))