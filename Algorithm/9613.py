from sys import stdin

input = stdin.readline

def gcd(a, b):
    if b>a:
        a, b = b, a

    while b!=0:
        a = a%b
        a, b = b, a

    return a

n = int(input())

for i in range(n):
    array = list(map(int,input().split()))
    cnt = 0

    for j in range(1,array[0]+1): #모든 경우의 수를 거친다.
        for k in range(j+1,array[0]+1): 
            cnt += gcd(array[j],array[k])

    print(cnt)