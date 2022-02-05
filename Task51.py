# 51 Составить список простых множителей натурального числа N
N = input(int('Введите числа  '))
list = []
while N > 0:    
    if N%2 == 0:
        list.append(2)
print(list)
