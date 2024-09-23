from sys import stdin

input = stdin.readline

def gcd(a, b):
    if b>a:
        a, b = b, a

    while b!=0:
        a = a%b
        a, b = b, a

    return a


a, b = map(int,input().split())

for i in range(gcd(a,b)):
    print(1,end='')