

N, M = map(int,input().split())

L = list(map(int,input().split()))

mi = 300000
q = 0

for i in range(len(L)):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            #print(L[i]+L[j]+L[k])
            if M-(L[i]+L[j]+L[k])<mi and M>=(L[i]+L[j]+L[k]):
                mi = M-(L[i]+L[j]+L[k])
                q = (L[i]+L[j]+L[k])
                #print(mi)
    
print(q)


'''
 합이 M보다 크지 않아야 한다는 조건을 파악하지 못했었다.
'''