


N, K = map(int,input().split())

c =0
count=1
num=0

L = [True for _ in range(N+1)]
print("<",end='')
while num<=N:
    if count%N==0:
        count=N
    else:
        count=count%N
        
    if L[count]:
        c+=1
    
    if L[count] and c%K==0:
        L[count]=False
        print(count,end='')
        if num!=len(L)-2:
            print(', ',end='')
            
        num+=1
    count+=1
    if num==len(L)-1:
        break
print('>')


'''
    좀 더 좋은 코드
    N, K = map(int, input().split())
    l = list(range(1, N+1))
    p = list()
    i = 0
    while l:
        i = (i+K-1) % len(l)
        p.append(str(l.pop(i)))

    print('<'+', '.join(p)+'>')
'''