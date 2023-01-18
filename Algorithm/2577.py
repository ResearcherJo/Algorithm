
a = int(input())
b = int(input())
c = int(input())

y = a*b*c

y = str(y)
g = [0,0,0,0,0,0,0,0,0,0]

for i in y:
    g[int(i)] += 1
    
for i in range(10):
    print(g[i])