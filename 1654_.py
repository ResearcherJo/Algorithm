from sys import stdin

input = stdin.readline

def Iterative(array,n):
    #start는 1, end는 가장 긴 랜선의 길이로 설정한다.
    start = 1
    end = max(array)
    m = 0

    while start<=end: #끝까지 탐색해보자.
        count = 0
        mid = (start+end)//2 #mid길이로 잘랐을때를 생각한다.

        #count에 mid로 잘랐을때 나오는 랜선의 개수를 저장
        for i in array:
            count+=i//mid

        #count가 구하려는 n개보다 크다면
        if count>=n:
            start = mid+1 #mid보다 긴 길이도 탐색해본다.
            m = mid #조건에 충족하는 길이 mid를 m에 저장한다.
        else:
            end = mid-1 #count가 n보다 작으면 길이를 줄여보자.

    return m

def recursive(array,start,end,n):
    if start>end: #start 가 end보다 크다면 end를 반환한다.
        return end
    
    count = 0
    mid = (start+end)//2

    #count에 mid로 잘랐을때 나오는 랜선의 개수를 저장
    for i in array:
        count+=i//mid

    if count>=n: #count가 구하려는 n개보다 크다면
        return recursive(array,mid+1,end,n)#mid보다 긴 길이도 탐색해본다.
    else: #count가 n보다 작으면 길이를 줄여보자.
       return recursive(array,start,mid-1,n)



k, n = map(int,input().split())
array = [int(input())for _ in range(k)]


#print(recursive(array,1,max(array),n))
print(Iterative(array,n))