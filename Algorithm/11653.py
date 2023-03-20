from sys import stdin

input = stdin.readline

n = int(input())
i = 2
while n!=1:
    if n%i == 0:
        print(i)
        n = n/i
    else:
        i+=1
        #그냥 2부터 나누어도 2의 배수로 다 나누고 못 나누는 수를 넘기기 때문에 2부터 나눠도 소수부터 나눈 것과 같은 효과가 있다.
'''
def prime_list(n):
    sieve = [False, False] + [True] * (n-1)

    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2,n+1) if sieve[i]==True]


n = int(input())

prime = prime_list(n)
i=0
while(n!=1):
    if n%prime[i]==0:
        print(prime[i])
        n/=prime[i]
    else:
        i+=1 
'''