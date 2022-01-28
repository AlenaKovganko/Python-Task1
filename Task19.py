# 19.пределить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
def Number(x, y):
    if x > 0 and y > 0: print('Первая четверть')
    elif x < 0 and y > 0: print('Вторая четверть')
    elif x < 0 and y < 0: print('Третья четверть')
    else: print('Четвертая четверть')
Number(x = int(input('Enter x:')), y = int(input('Enter y:')))