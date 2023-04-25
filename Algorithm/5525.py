from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
S = input()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI': #3칸
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)


'''
from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
P = 'I' + 'OI'*N
P = input()
count = 0



for i in range(M):
    if P[i] == P[0]: #시작이 같다면
        k = 0
        for j in range(i,i+(N*2+1)): #나머지도 같은지 비교
            if P[j]!=P[k]:
                break
            k+=1
        else: #나머지도 같다면 count+1해준다.
            count+=1

print(count)
'''