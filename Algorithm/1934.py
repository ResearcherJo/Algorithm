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

    a, b = map(int,input().split())

    print((a*b)//gcd(a,b))