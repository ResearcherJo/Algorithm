





n = int(input())



l=list()

for i in range(n):
    l.append(int(input()))

d = [0]*(max(l)+2)
d[1] = 1
d[2] = 1
    
for i in range(3,max(l)+2) :
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in range(n):
    print(d[l[i]+1])

'''

    규칙 찾기 힘들다....

'''