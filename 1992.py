import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def quad(array, x, y, n):

    key = array[y][x]
    
    for i in range(y,y+n):
        for j in range(x,x+n):
            if key!=array[i][j]:
                next = n//2
                print('(',end='')#나눠짐을 의미한다.
                quad(array,x+(next*0),y+(next*0),next) #2사분면
                quad(array,x+(next*1),y+(next*0),next) #1사분면
                quad(array,x+(next*0),y+(next*1),next) #3사분면
                quad(array,x+(next*1),y+(next*1),next) #4사분면
                print(')',end='')
                return
            
    print(key,end='')
    return

n = int(input())
array = [list(input()) for _ in range(n)]

quad(array,0,0,n)