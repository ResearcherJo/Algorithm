from sys import stdin

input = stdin.readline

#합치는 함수
def merge(arr, start, mid, end):
    global count
    left = start #왼쪽 리스트 시작 index
    right = mid+1 #오른쪽 리스트 시작 index
    r_index = start #arr의 실제 index
    
    while left<=mid and right<=end:
        if arr[left]<=arr[right]:#왼쪽 리스트가 가리키는 원소가 작다면
            result[r_index] = arr[left]
            left+=1
        else:#오른쪽 리스트에서 가리키는 원소가 작다면
            result[r_index] = arr[right]
            right+=1
            count += mid-left+1 #왼쪽 정렬의 남은 원소개수를 더한다.
        r_index+=1
    
    if left>mid: #오른쪽 리스트에 원소가 남아있다면 넣는다.
        for i in range(right,end+1):
            result[r_index] = arr[i]
            r_index+=1
    else: #왼쪽 리스트에 원소가 남아있다면 넣는다.
        for i in range(left,mid+1):
            result[r_index] = arr[i]
            r_index+=1

    #왼쪽 리스트와 오른쪽 리스트가 정렬된 result를 arr에 옮긴다.
    for i in range(start,end+1):
        arr[i] = result[i]

#쪼개는 함수
def mergesort(arr, start, end):
    if start<end:
        mid = (start+end)//2
        mergesort(arr,start, mid) #왼쪽으로 쪼갬
        mergesort(arr,mid+1, end) #오른쪽으로 쪼갬
        merge(arr,start,mid,end) #다 쪼갠 후 붙임

n = int(input())
arr = list(map(int,input().split()))
result = [0 for _ in range(n)]
count = 0

mergesort(arr,0,n-1) #배열, 인덱스 : 0~(n-1)까지의 

print(count)
