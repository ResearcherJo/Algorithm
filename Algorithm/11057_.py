


def d (dp,dp_n,n):
    l = list()
    for k in range(n):
        for i in range(len(dp)):
            for j in dp[i]:
                if j!=9:
                    for k in range(j+1,10):
                        l.append(k)
            
            dp[i]=l.copy()
            l.clear()
    s=0
    
    print(dp)
    print(len(dp[0]))
    for i in dp:
        s+=len(i)
    print(s)
                




    
    
dp =[[i]for i in range(10)]

dp_n=[0 for i in range(10)]

d(dp,dp_n,2)



