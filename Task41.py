# 41 Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
list = ['a', 'b', 'c', 'd', 'a']


def find(text):
    res = 0
    for i in range(0, len(list)):
        if text == list[i]:
            res += 1
            if res == 2:
                print(i)
    if res < 2:
        print('Второго вхождения нет')


find(text=(input('Введите  ')))
