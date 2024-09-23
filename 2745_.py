

from sys import stdin, stdout

input = stdin.readline

system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
result = 0

for i in range(len(n)):
    result += system.index(n[i])*(int(b)**(len(n)-1-i))
print(result)


'''
    새로운 진수에 대한 개념을 알게 되었고, 그걸 이용할 수 있었다. https://growingarchive.tistory.com/208 8을 2진수로 바꿀려면 1000 = (1*2^3)+(0*2^2)+(0*2^1)+(0*2^0) = 8 인것을 이용한것이다.
    진수라는 수학적 개념에 대해 알아야 될 것 같다.
'''

from sys import stdin

input = stdin.readline

n, b = input().split()

print(int(n,int(b)))