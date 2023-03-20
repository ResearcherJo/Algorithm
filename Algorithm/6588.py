from sys import stdin

input = stdin.readline

def prime_list(n):
    sieve = [False, False] + [True]*(n)

    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j] = False

    return sieve


array = prime_list(1000000)
dis = [i for i in range(2, 1000000+1)if array[i]==True]

while True:
    n = int(input())
    if n==0:
        break

    for i in range(len(dis)):
        if dis[i]>n:
            print("Goldbach's conjecture is wrong.")
            break

        if dis[i]%2!=0 and array[n-dis[i]]:
            print("{0} = {1} + {2}".format(n,dis[i],n-dis[i]))
            break
