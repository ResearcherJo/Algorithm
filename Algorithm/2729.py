from sys import stdin, stdout

input = stdin.readline

def two(x):
    return int(x,2)

for _ in range(int(input())):
    a, b = map(two,input().split())
    print(bin(a+b).replace("0b",""))
    