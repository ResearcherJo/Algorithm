from sys import stdin

input = stdin.readline

n = int(input())
array = list(map(int,input().split()))

max = max(array)

# 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
# 체를 1부터 계산하기 위해 [False,False]로 초기화 1은 소수가 아니기때문에 False
# [False,False]를 미리 추가하므로 max에 1을 빼준다.
sieve = [False,False] + [True] * (max-1)

m = int(max ** 0.5)

for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우            
            for j in range(i+i, max+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

count = 0
for i in array:
    if sieve[i]:
        count+=1

print(count)