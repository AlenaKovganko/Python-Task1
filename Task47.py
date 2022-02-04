# Строка содержит набор чисел. Показать большее и меньшее число
A = input('Введите числа  ').split()
for i in range(len(A)):
    A[i] = int(A[i])
print(A)