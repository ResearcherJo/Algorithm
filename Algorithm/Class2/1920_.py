

N = int(input())

A = list((map(int,input().split())))
A.sort()
M = int(input())
K = list(map(int,input().split()))

for i in K:
    start = 0
    end = len(A)-1
    count=0
    while start<=end:
        mid = (start+end)//2
        if i==A[mid]:
            count=1 
            break
        elif i>A[mid]:
            start = mid+1
        else:
            end = mid-1
        
    if count==1:
        print('1')
    else:
        print('0')
        
'''
    문제 조건에 정수라고 있는건 음의 정수만 있는 것은 아니다.
'''