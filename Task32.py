# 32 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.
def dictionary(N):
    d = {}
    for k in range(1, N + 1):
        d[k] = (3 * k) + 1   
    return d
print(dictionary(N = int(input('Введите N '))))






