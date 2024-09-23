

T = int(input())

'''
0 1 2 3 4 5
0 1 3 6 10 15
0 1 4 10 20 35
'''

for i in range(T):
    K = int(input())
    N = int(input())
    count = [[0] * (N+1) for _ in range(K+1)]
    for j in range(K+1):
        for k in range(1,N+1):
            if j == 0:
                count[j][k]=k
            else:
                count[j][k] = count[j-1][k]+count[j][k-1]
    print(count[K][N])
        
    
    