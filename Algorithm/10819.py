from sys import stdin

input = stdin.readline

#순열을 구하는 함수
def perm(arr,n):
    result = []
    
    #1개만 보면 그냥 result에 넣고 끝낸다.
    if n==1:
        result.append(arr)
    elif n>1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            #i번째 원소를 제외한다. i : 0~n-1
            ans.remove(arr[i])

            for p in perm(ans,n-1):
                #i번째 원소에 n-1개의 섞인 리스트를 합친다.
                result.append([arr[i]]+p)
    
    return result

n = int(input())
arr = list(map(int,input().split()))
arr = perm(arr,n)
ma = 0

#모든 경우의 수에 대해 계산값을 구한다.
for i in arr:
    sum = 0
    for j in range(n-1):
        sum += abs(i[j]-i[j+1])
    #계산 값중에 최댓 값을 ma에 갱신한다.
    ma = max(ma,sum)

print(ma)