

N = int(input())

l = [0,-1,-1,1,-1,1]+[0 for _ in range(N+1-6)]
    
for i in range(3,N+1):
    count = 0
    n = i
    while True:
        if l[n]>0:
            count+=l[n]
            l[i]=count
            break
        if l[n-5]!=-1 and n>=5:
            count+=1
            n-=5
        elif l[n-3]!=-1 and n>=3:
            count+=1
            n-=3
        else:
            l[n]=-1
            break
print(l[N])
            
            
            
'''



'''
                