'''
풀이
https://velog.io/@babnbabn/2447번-별-찍기-10-Python
'''
from sys import stdin
input = stdin.readline

def solve(arr, x, y, n):

    if n == 1: #1칸을 바라볼때
        arr[y][x] = '*'
        return
    
    next = n//3

    solve(arr, x + (next*0),y + (next*0),next) #북서
    solve(arr, x + (next*1),y + (next*0),next) #북
    solve(arr, x + (next*2),y + (next*0),next) #북동

    solve(arr, x + (next*0),y + (next*1),next) #서
    #solve(arr, x + (next*1),y + (next*1),next)#center
    solve(arr, x + (next*2),y + (next*1),next) #동

    solve(arr, x + (next*0),y + (next*2),next) #남서
    solve(arr, x + (next*1),y + (next*2),next) #남
    solve(arr, x + (next*2),y + (next*2),next) #남동

N = int(input())
# 출력 결과의 틀을 만들어둔다.
arr = [[' ' for _ in range(N)] for _ in range(N)]

solve(arr, 0,0,N)

for i in arr:
    for j in i:
        print(j, end='')
    print()
