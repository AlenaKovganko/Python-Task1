# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
def multiplicity(a):
    if a%10==0: print('Число кратно 10')
    else: print('Число некратно, остаток',a%10)

multiplicity(a = int (input('введите число ')))