from sys import stdin

input = stdin.readline


#별그리는 함수 / y : 좌표 y값, x : 좌표 x값, size : N값
def star(y, x, size):
    #size가 3이면 가장 기본적인 *이 찍힌다.
    if size==3:
        array[y][x] = '*'
        array[y+1][x-1] = array[y+1][x+1] = '*'
        for i in range(-2,3):
            array[y+2][x+i] = '*'
    else:
        #size는 /2씩 감소한다.
        next_size = size//2
        
        #3개로 나눈다.
        star(y,x,next_size) #가운데
        star(y+next_size,x+next_size,next_size) #오른쪽
        star(y+next_size,x-next_size,next_size) #왼쪽

N = int(input())
array = [[' ']*N*2 for _ in range(N)]

star(0,N-1,N)

for i in range(N):
    print(''.join(array[i]))

