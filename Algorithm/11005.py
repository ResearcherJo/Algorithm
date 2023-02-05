from sys import stdin
input = stdin.readline


system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #36진수까지의 경우를 저장해 둔다.

n, b = map(int,input().split())
result = ''

while n!=0:
    result += system[n%b]
    n//=b
    
print(result[::-1]) #저장이 거꾸로 되기 때문에 뒤집어서 출력해준다.