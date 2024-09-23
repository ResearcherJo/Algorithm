from sys import stdin, stdout

input = stdin.readline 


n = int(input().rstrip())

for i in range(n):
    a, b = map(int,input().split())
    print(a+b)
