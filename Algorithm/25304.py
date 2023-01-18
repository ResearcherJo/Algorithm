from sys import stdin, stdout

input = stdin.readline 
print = stdout.write


result = int(input())

n = int(input())

sum = 0

for i in range(n):
    a, b = map(int,input().split())
    sum += a*b
    
if sum==result:
    print('Yes')
else:
    print('No')