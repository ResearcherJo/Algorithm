'''
    1이 될 때까지
    
    어떤수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고한다. 단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
    1. N에서 1을 뺀다.
    2. N을 K로 나눈다.
    
    예를 들어 N = 17, K = 4일 경우
    1) 17 - 1 = 16
    2) 16 // 4 = 4
    3) 4 // 4 = 1

    전체 과정을 실행한 횟수는 3이 된다. 이는 N을 1로 만드는 최소 횟수이다. 
'''

N, K = map(int, input().split())

count = 0

while N!=1:
    if N%K==0:
        count+=1
        N//=K
    else:
        count+=1
        N-=1
        
print(count)

'''
    #N, K를 공백을 기준으로 구분하여 입력 받기
    N, K = map(int,input().split())
    
    result = 0
    
    while True : #while문 한번돌때마다 N이 나눠지기 때문에 훨씬 효율적
        #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
        target = (N//K)*K
        result += (N-target)
        N = target
        
        #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if N<K:
            break
        
        #K로 나누기
        result +=1
        N//=K
        
    #마지막으로 남은 수에 대하여 1씩 빼기
    result+=(N-1)
    print(result)
'''