


N, M = map(int,input().split())

l = list(map(int,input().split()))

start = 1
end = max(l)

while start<=end:
    mid = (start+end)//2
    count = 0
    for i in l:
        if i>=mid:
            count+=i-mid
    
    if count>=M:
        start = mid+1
    else:
        end = mid-1
print(end)