f = open('//book/!-Буфер/Пб/Задачи/ГИТ/Задание 2/Perepis.txt', 'r')


count = 0

for i in f:
    s = i.split()
    if int(s[3][6:]) < 1978:
        print(s[0], s[1], s[2])
        count += 1
print(count)

f.close()


f = open('//book/!-Буфер/Пб/Задачи/ГИТ/Задание 2/Perepis.txt', 'r')
a = int(input('С какого года'))
b = int(input('До какого года'))

for i in f:
    s = i.split()
    if (int(s[3][6:]) > a) and (int(s[3][6:]) < b):
        print(s[0], s[1], s[2])

f.close()



