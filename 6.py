f = open('//book/!-Буфер/Пб/Задачи/ГИТ/Задание 2/Perepis.txt', 'r')

l = [elem for elem in f]
count = 0

for i in l:
    s = i.split()
    if int(s[3][6:]) < 1978:
        print(s[0], s[1], s[2])
        count += 1
print(count)

    
        
    
a = int(input('С какого года'))
b = int(input('До какого года'))

for i in l:
    if (int(s[3][6:]) > a) and (int(s[3][6:]) < b):
        print(s[0], s[1], s[2])
        

    
