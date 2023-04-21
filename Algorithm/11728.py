from sys import stdin

input = stdin.readline


n, m  = map(int,input().split())
a_index = 0
b_index = 0
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list()

while a_index<n and b_index<m:
    if a[a_index]>b[b_index]:
        c.append(b[b_index])
        b_index+=1
    elif a[a_index]<b[b_index]:
        c.append(a[a_index])
        a_index+=1
    elif a[a_index]==b[b_index]:
        c.append(a[a_index])
        c.append(b[b_index])
        a_index+=1
        b_index+=1


for i in range(b_index,m):
    c.append(b[i])
for i in range(a_index,n):
    c.append(a[i])

print(*c)
