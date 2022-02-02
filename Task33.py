# 33 Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
def string(str1, str2):
    count = 0
    symbol = ''
    u = 0
    while u < len(str2):
        for i in str1:
            for j in str2:
                if i==j:
                    count+=1
        u+=1
    return(count // u) // u
print(string(str1 = input('Введите строку 1 '),str2 = input('Введите строку 2 ')))