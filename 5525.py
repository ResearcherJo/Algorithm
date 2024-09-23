from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
S = input()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI': #IOI라면
        count += 1 #IOI의 개수를 count해준다.
        cursor += 2 #IOIOI에서 IOI를 2개있다고 보기 위해서 +2해준다.
        if count == N: # IOI가 N번 있으면 result를 증가 시킨다.. 
            result += 1
            count -= 1 #다시 IOI가 바로 뒤에 붙어있어도 되기 때문에 이를 count하기 위해서 -1해준다.

    else:#IOI가 아니라면 다시 처음부터 시작한다. cursor는 한칸 증가시킨다.
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