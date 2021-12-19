


n = int(input())
count=0
a = n**(1/2)

while True:
    print(n) 
    if n == 0:
        break
    
    if a-int(a)==0:
        n-=a**2
        count+=1
        a = n**(1/2)
    else:
        a-=1

print(count)

'''

    자연수 n이 주어질 때, n을 최소 개수의 제곱수 합(<=4)으로 표현하는 문제이다.
    dp를 사용하여 2부터 리스트의 값을 채워간다.
    n이 제곱수라면 dp[i] = 1
    n이 제곱수가 아니라면 n과 가장 가까운 제곱수 값을 찾기 위해 i를 1씩 증가시키고 j의 값을 1부터 제곱근 i의 정수값 까지 증가시키면서 dp[i]가 가질 수 있는 최소값을 채워준다.


    import math

    def is_square(n):
        return int(n ** 0.5) ** 2 == n 
    
    n = int(input())
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    
    i = 2
    while i <= n: 
        if is_square(i):
            dp[i] = 1
        else:
            dp[i] = i
        i += 1
        
    i = 2
    while i <= n:
        j = 1
        while j <= int(math.sqrt(i)):
            dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
            j += 1
        i += 1
    
    print(dp[n])
    
'''