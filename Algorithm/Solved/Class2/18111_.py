import sys

N, M, B = map(int,input().split())

L = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]

start = min(map(min, L))
end = max(map(max, L))
count = [1000000000000000,-1]

for i in range(start,end+1):
    time = 0
    Block = B
    for j in L:
        for k in j:
            if k<i:
                Block-=(i-k)
                time+=1*(i-k)
            elif k>i:
                Block+=(k-i)
                time+=2*(k-i)
    
    if Block>=0 and time<=count[0]:
        count[0]=time
        if count[1]<=i:
            count[1]=i
        

print(count[0],count[1])


'''
    최소 값을 찾으려고 큰 값을 이용하려 한다면 진짜 큰 값을 쓰자... 괜히 9999같은 이상한 값 쓰지 말자...
'''