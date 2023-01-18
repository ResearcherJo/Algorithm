

N = int(input())

L = list()

for i in range(N):
    New = list(map(int,input().split()))+[0]+[i]
    L.append(New)
    
L.sort(key = lambda x : x[1],reverse = True)
L.sort(key = lambda x : x[0],reverse = True)

L[0][2] = 1
rank = 1

for i in range(1,len(L)):
    rank=1
    for j in range(0,i):
        if L[j][0]>L[i][0] and L[j][1] > L[i][1]:
            rank= rank+1
    L[i][2] = rank    
        
        
L.sort(key = lambda x:x[3])

for i in L:
    print(i[2],end=' ')
    
'''
    괜히 시간초과 걱정함;;
    
    
    좀 더 좋은 코드
    
    num=int(input())
    val=[]
    for i in range(num) :
        val.append(list(map(int,input().split())))

    for i in val :
        rank=1
        for j in val :
            if i[0] < j[0] and i[1] < j[1]:
                    rank += 1
        print(rank,end=' ')
'''
    