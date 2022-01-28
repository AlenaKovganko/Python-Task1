# По заданному номеру дня недели вывести его название
def numberDay(a):
    if a == 1: print ('Понедельник')
    elif a == 2: print ('Вторник')
    elif a == 3: print ('Среда')
    elif a == 4: print ('Четверг')
    elif a == 5: print ('Пятница')
    elif a == 6: print ('Суббота')
    elif a == 7: print ('Суббота')
    else: print ('Номер некорректен')
numberDay (a = int(input('Введите номер дня недели ')))
