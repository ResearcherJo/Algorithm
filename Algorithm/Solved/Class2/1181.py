

n = int(input())

l = list()

for i in range(n):
    l.append(input())
l=set(l)
l=list(l)
l.sort()
l.sort(key=len)


for i in l:
    print(i)