from sys import stdin

input = stdin.readline

#에타로스테네스의 체를 이용해 소수를 구하는 함수
def prime_list(n):
    sieve = [False, False] + [True]*(n)

    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j] = False

    return sieve


array = prime_list(1000000) #소수인지 아닌지 True와 False로 판단한다.
dis = [i for i in range(2, 1000000+1)if array[i]==True] #소수인 값들만 가지고 있는 배열

while True:
    n = int(input())
    if n==0:
        break

    for i in range(len(dis)):
        if dis[i]>n: # 만약 i번째 소수의 값이 n을 넘는 다면 
            print("Goldbach's conjecture is wrong.")
            break

        if dis[i]%2!=0 and array[n-dis[i]]: #i번째 소수가 홀수 이고, (n - i번째 소수)도 홀수라면 출력한다. 
            print("{0} = {1} + {2}".format(n,dis[i],n-dis[i]))
            break
