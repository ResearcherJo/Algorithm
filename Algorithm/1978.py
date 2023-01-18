

N = int(input())

l = list(map(int,input().split()))

prime = [False,False] + [True]*(max(l)-1)
m = int(max(l)**0.5)

for i in range(2, m+1):
    if prime[i]:
        for j in range(i*2,max(l)+1,i):
            prime[j] = False
              
count = 0
                   
for i in l:
    if prime[i]:
        count+=1
        
print(count)