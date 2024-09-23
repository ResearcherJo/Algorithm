

n = int(input())

count = (1+n)*(n//2)
if n%2!=0:
    count+=n//2+1
    
print(count)