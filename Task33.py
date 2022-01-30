# 33 Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
def string(string1, string2):
    s1 = set(string1)
    s2 = set (string2)
    i = s1.intersection(s2) 
    return(i)
print(string(string1 = input('Введите строку 1 '),string2 = input('Введите строку 2')))