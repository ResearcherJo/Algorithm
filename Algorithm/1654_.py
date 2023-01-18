

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
    
    if count>=K:
        start = mid+1
        key = mid
    else:
        end = mid-1


print(key)

'''
    이분탐색(Binary Search)에 더한 매개변수탐색(Parametric Search)을 이용
    굳이 리스트를 활용할 필요는 없다. 오히려 메모리 초과를 불러온다.
    https://claude-u.tistory.com/443에서는 end가 정답이라고 했는데 그 이유는 아직 모르겠다.
    이분탑색할때 범위를 잘 고려해야 한다.
'''
