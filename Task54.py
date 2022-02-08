# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
with open("54_1.txt", "r") as file:
    polynomial1 = file.read()
    print(f'первый многочлен {polynomial1}')
with open("54.2.txt", "r") as file:
    polynomial2 = file.read()
    print(f'второй многочлен {polynomial2}')
str = polynomial1 + '+' + polynomial2
str = str.replace('+',' ').replace('-',' ')
str = str.split()
print(str)
x0 = [] 
x = []
x2 =  []
c = 'x' 
c2 = 'x**2'
sum0 = 0
sum1 = 0
sum2 = 0
for i in str:
    if c2 in i : x2.append(i)
    if c in i and c2 not in i : x.append(i)
    if c not in i: x0.append(i)
for i in x2: 
    i2 =i.replace('x**2','')
    sum2 = sum2+int(i2)
for i in x: 
    i2 =i.replace('x','')
    sum1 = sum1 + int(i2)
for i in x0: 
    i2 =i.replace('x','')
    sum0 = sum0+int(i2)
str = f'{sum2}x**2 + {sum1}x +{sum0}'
print(f'сумма {str}')

with open("54.3.txt", "w") as somefile:
    somefile.write(str) 