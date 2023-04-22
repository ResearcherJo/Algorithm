from sys import stdin

input = stdin.readline

def div(x,y,n):
    if (x//n)%3==1 and (y//n)%3==1:
        print(' ',end='')
    else:
        if n==1:
            print('*',end='')
        else:
            div(x,y,n//3)


n = int(input())

for i in range(n):
    for j in range(n):
        div(j,i,n)
    print()