# 55. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# тобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('55.txt', 'r') as file :
    str = file.read()
print(f'строка из файла {str}') 
str = str.split()

for i in range(1,len(str)): 
    if not int(str[i]) - 1 == int(str[i-1]): 
        print(f'недостающее число {int(i+1)}')

