from sys import stdin, stdout

input = stdin.readline 
print = stdout.write

n = int(input())

for i in range(n):
    a = input()
    print(a.strip()[0]+a.strip()[-1]+'\n')