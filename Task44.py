# 44 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list = [1.1, 1.2, 3.1, 5, 10.01]
float_list = [round(item % 1, 2) for item in list] # остаток деления на 1
print(float_list)
print(f'{max(float_list) - min(float_list) : .2f}')