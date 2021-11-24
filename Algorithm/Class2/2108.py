
n = int(input())

l = list()

for i in range(n):
    l.append(int(input()))
    
print(round(sum(l)/len(l)))
l.sort()
print(l[len(l)//2])

d = dict()

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

d = sorted(d.items(), key=lambda x: x[1],reverse = True)

if len(d)<2:
    print(d[0][0])
else: # 무조건 d[1][0]을 출력하면 빈도수가 달라질 수 있기 때문에 빈도수가 같은지도 확인해야 한다.
    if d[0][1]==d[1][1]:
        print(d[1][0])
    else:    
        print(d[0][0])

print(max(l)-min(l))
