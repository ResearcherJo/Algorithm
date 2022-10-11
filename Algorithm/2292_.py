

N = int(input())


if N!=1:
    last = 1
    for i in range(1,N):
        if (1+(6*(i-1))+1)<=N and (last+6*i)>=N:
            print(i+1)
            break
        last = last+6*i
    
else:
    print('1')
'''
    1을 입력했을때 0이냐 1이냐에서 좀 햇갈렸던거 같다. 이것 또한 문제를 제대로 읽지 않아서 그런거 같다. 정말 슬프다. 어제 풀 수 있었는데...
'''