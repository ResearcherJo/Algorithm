from sys import stdin, stdout

input = stdin.readline 

def sieve(n, m):
    l = [False, False] + [True]*(m)

    k = int(m**0.5)
    for i in range(2, k+1):
        if l[i]:
            for j in range(i+i,m+1,i):
                l[j] = False

    return [i for i in range(n, m+1) if l[i] == True]

n, m = map(int,input().split())

array = sieve(n, m)
for i in array:
    print(i)

