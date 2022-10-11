
from sys import stdin, stdout

input = stdin.readline 


p = [0,0,0,0,0,0,0]

a, b, c = map(int,input().split())

p[a] += 1
p[b] += 1
p[c] += 1

if 3 in p:
    print(10000+a*1000)
elif 2 in p:
    print(1000+p.index(2)*100)
else:
    print(max(a,b,c)*100)

