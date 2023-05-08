from sys import stdin

input = stdin.readline

N  = int(input())
arr = list(map(int,input().split()))
s = 0

#오름차순으로 정렬
arr.sort()

#정렬된 값을 더한다.
for i in range(1,N+1):
    s+=sum(arr[0:i])

print(s)