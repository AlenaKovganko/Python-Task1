# Удалить вторую цифру трёхзначного числа
number = input('Введите число a ')
spisok = list (number)
spisok.remove(spisok[1])
print(spisok)