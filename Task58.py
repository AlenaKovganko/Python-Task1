# 58. Напишите программу, удаляющую из текста все слова содержащие "абв"
def delete(text):
    str = text.split(" ")
    str2 = []
    temp = 'абв'
    print(str)
    for i in range (0, len(str)):
        if not temp in str[i]:
            str2.append(str[i])
    str2 = ' '.join(str2) 
    print(str2)
text  = 'Напишите программу, удаляющую из текабвста все слова содержащие абв'
delete(text)
