

n = int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    if i==1:
        print('*')
    elif i==n:
        print('*'*(2*n-1),end='')
    else:
        print('*'+' '*(i*2-3)+'*')
        
        
        
'''
    좀 더 반복문을 덜 쓰고, 수학적으로 풀 수 있는 방법을 알아보자
    N = int(input())
    
    if N == 1:
        print('*')
    else:
        print(' ' * (N - 1) + '*')
        for i in range(N - 2):
            print(' ' * (N - i - 2) + '*' + ' ' * (2 * i + 1) + '*')
        print('*' * (2 * N - 1))
'''