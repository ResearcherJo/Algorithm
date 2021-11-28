

N = int(input())

NL = list(map(int,input().split()))

NL_D = dict()

for i in NL:
    if i in NL_D:
        NL_D[i]+=1
    else:
        NL_D[i]=1

M = int(input())

ML = list(map(int,input().split()))

for i in ML:
    if i in NL_D:
        print(NL_D[i],end=' ')
    else:
        print('0',end=' ')


'''
    해쉬테이블은 파이썬으로 딕셔너리로 구현할 수 있고, 그러면 더 빠르게 처리할 수 있다.
'''