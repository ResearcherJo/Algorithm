from collections import deque
from sys import stdin

input = stdin.readline

sieve = [True] * 10000

#에라토스테네스의 체를 만든다.
def make_sieve():
    m = int(10000 ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, 10000, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

def bfs(n,end):

    #visited 와 queue 초기화
    visited = [0] * 10000
    queue = deque()

    queue.append([n,0]) #시작값을 queue에 넣어준다. 횟수는 0부터 시작이다.

    while queue:
        x, cnt = queue.popleft() #x에는 비밀번호를 cnt에는 바꾼 횟수를 저장한다.
        now = str(x)

        #비밀번호가 바꾸고자 하는 비밀번호라면 횟수를 출력하고 return한다.
        if x == end:
            print(cnt)
            return
        
        #총 4자리의 값들을 바꿔야 한다.
        for i in range(4):
            #각 자리의 값을 0~9까지 바꿔야 한다.
            for j in range(10):
                #배열을 이용해서 i번째 자리의 숫자를 바꿔서 temp에 저장한다.
                temp = int(now[:i] + str(j) + now[i+1:])

                #temp에 저장한 값이 가본 적이 없고, 소수이면서 1000보다 크다면 바꾸고, 변경횟수를 1증가시킨다.
                if visited[temp] == 0 and sieve[temp] and temp>=1000:
                    visited[temp] = 1
                    queue.append([temp,cnt+1])

t = int(input())

make_sieve()

for i in range(t):
    s, e = map(int,input().split())
    bfs(s,e)    