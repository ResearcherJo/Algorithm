'''
    이분탐색 알고리즘을 이야기할 때 함께 나오는 탐색 방법인 매개변수 탐색(Parametric Search)는 이분탐색과 상당히 유사합니다.
    두 개념을 구분하지 않고 이분탐색의 방법으로 매개변수 탐색(Parametric Search)를 소개하기도 합니다.
    다만 차이점이라고 한다면 이분탐색은 원하는 조건을 찾으면 바로 결과값을 반환하고 종료하는 알고리즘이지만 매개변수 탐색(Parametric Search)는 조건을 만족시킨 이후에도 최대, 최소를 찾기 위해 끝까지 탐색을 계속합니다
'''

#1654 랜선자르기 문제

N, K = map(int,input().split())
N_list = list()

for i in range(N):
    N_list.append(int(input()))
    
N_list.sort()


start = 1
end = N_list[N-1]


mid = (start+end)//2
key=0
while start<=end:
    mid = (start+end)//2
    count = 0
    
    for i in N_list:
        count+=i//mid
    
    if count>=K: #원하는 조건을 만족해도 최대 혹은 최소를 찾기위해 계속 탐색한다. 그러기 위해서 >가 아닌 >=이다.
        start = mid+1
        key = mid    
    else:
        end = mid-1


print(key)