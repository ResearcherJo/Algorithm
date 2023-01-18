

n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

i=0
j=0


while i<len(a):
    
        if a[i]>=b[j]:
            a[i]-=b[j]
            if j+1<len(b):
                j+=1
            else:
                break
        else:
            i+=1
    
print(sum(a))