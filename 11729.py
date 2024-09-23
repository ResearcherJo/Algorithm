import sys

input = sys.stdin.readline

def hannoi(n,f,w,to):
    if n==0:
        return
    else:
        hannoi(n-1,f,to,w)
        print('{} {}'.format(f,to))
        hannoi(n-1,w,f,to)

n = int(input())

print(2**n-1) # 최소이동 횟수
hannoi(n,1,2,3)
