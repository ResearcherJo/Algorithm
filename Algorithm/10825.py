from sys import stdin

input = stdin.readline

n = int(input())

array = [list(input().split()) for i in range(n)]

'''
array.sort(key=lambda x:x[0])
array.sort(key=lambda x:int(x[3]),reverse=True)
array.sort(key=lambda x:int(x[2]))
array.sort(key=lambda x:int(x[1]), reverse=True)
'''
array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
#  -를 붙이면 내림차순으로 정렬하게 된다. 앞에 있는 기준부터 순서대로 정렬하게 된다.

for i in range(n):
    print(array[i][0])