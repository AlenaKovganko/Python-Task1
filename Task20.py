# 20. Задать номер четверти, показать диапазоны для возможных координат
def Number(a):
    if a == 1: print('x > 0 and y > 0')
    elif a == 2: print('x < 0 and y > 0')
    elif a == 3: print('x < 0 and y < 0')
    elif a == 4: print ('x > 0 and y < 0')
    else: print('Номер некорректен')
Number(a = int(input('Введите номер четверти  ')))