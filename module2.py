f = open('travels.txt', 'r')


count = 0

for i in f:
    s = i.split()
    for i in f:
        maxn = max(s[6])
        print(maxn)

f.close()


