# 31 для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
def create_list(N = 10): 
    list_N = [] 
    res = 1
    for i in range(0, N):
        if len(list_N) % 2:
            res = -3 ** i
            list_N.append(res)
        else: 
            res = 3 ** i
            list_N.append(res)
    return list_N
print(create_list(N = int(input('Введите N '))))