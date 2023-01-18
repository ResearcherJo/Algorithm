
from sys import stdin
input = stdin.readline


system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int,input().split())
result = ''

while n!=0:
    result += system[n%b]
    n//=b
    
print(result[::-1])

'''
    진수 변화의 원리를 알게된다면 좀더 좋았을것 같다. 진수는 바꾸려는 수(X)를 바꾸고 싶은 진수(Y)로 나누었을때 나머지로 결정된다. 그 수가 숫자로 나온다면 system처럼 문자열을 ㅁ나들어서 문자로 변환하는 과정을 거치자
    그렇게 나머지들을 뒤에서 부터 출력하면 된다. 그냥 2진수를 바꾸는 방법과 다르지 않다. 2진수가 n진수로 바뀌었을뿐

'''