# 42 Найти сумму чисел списка стоящих на нечетной позиции

list = [3, 1, 8 ,1 ,9 , 1]
sum = 0
for i in range(len(list)):
    if i%2 !=0:
        sum += list[i]
print(sum)

