# 56. Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
A = [1, 5, 2, 3, 4, 6, 1, 7]
l = len(A)-1
print(A)
for i in range (1,len(A)-1):
    if  i > i-1:
        A.remove(i)
print(A)