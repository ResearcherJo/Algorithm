from sys import stdin

input = stdin.readline

def z(x, y, n):
    global count
    if n==2: #(2,2)안에 r, c가 있다면 찾은 뒤 출력한다.
        for i in range(y,y+2):
            for j in range(x,x+2):
                if i==r and j==c:
                    print(count)
                    exit(0)
                count+=1

    else:
        next = n//2
        if y<=r<y+(next) and x<=c<x+(next):     #2사분면
            z(x,y,next)
        elif y<=r<y+(next) and x+(next)<=c<x+n: #1사분면
            count += next*next #2사분면을 건너뛴거니 그 만큼 더해준다.
            z(x+(next),y,next)
        elif y+(next)<=r<y+n and x<=c<x+(next): #3사분면
            count += next*next*2 #1,2사분면을 건너뛴거니 그 만큼 더해준다.
            z(x,y+(next),next)
        else:                                   #4사분면
            count += next*next*3 #1,2,3사분면을 건너뛴거니 그 만큼 더해준다.
            z(x+(next),y+(next),next)

n, r, c = map(int,input().split())

count = 0
z(0,0,2**n)