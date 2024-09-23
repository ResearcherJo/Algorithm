from sys import stdin

input = stdin.readline

korea = 'KOREA'
yonsei = 'YONSEI'

k = 0
y = 0

array = input()

for i in array:
    if i == korea[k] and i == yonsei[y]:
        k+=1
        y+=1
    elif i == korea[k]:
        k+=1
    elif i == yonsei[y]:
        y+=1

    if k==5:#KOREA의 길이
        print(korea)
        break
    elif y==6:#YONSEI의 길이
        print(yonsei)
        break
    