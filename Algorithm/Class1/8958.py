

n = int(input())


l = list()
for i in range(n):
    st = input()
    l.clear()
    count = 0
    for j in st:
        if j=='O':
            l.append('O')
        else:
            l.clear()
        count+=len(l)
    print(count)