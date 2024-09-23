from sys import stdin

input = stdin.readline
    
a, b = map(int, input().split())    

def gcd(a, b):
    if(b>a) : a,b = b,a

    while(b!=0):
        a=a%b
        a,b=b,a
        
    return a

g = gcd(a,b)

print(g)
print(a*b//g)

#유클리드 호제법으로 최대 공약수를 구한뒤 a*b의 곲을 최대 공약수로 나눈다면 최소 공배수가 나온다.