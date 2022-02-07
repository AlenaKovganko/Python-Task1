# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

k = 2
list = []
for i in range (0,k+1):
    list.append(randint(0,100))
print(list)

print(f'{list[0]}*x**{i}+{list[1]}*x + {list[2]} = 0')
with open('53.txt', 'w') as file:
    file.write

    





