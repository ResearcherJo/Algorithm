from sys import stdin
from collections import deque


#L명령어 수행하는 함수
def L(n):
    front = n%1000
    back = n//1000
    res = front*10 + back
    return res

#R명령어 수행하는 함수
def R(n):
    front = n%10
    back = n//10
    res = front*1000 + back
    return res

#D명령어 수행하는 함수
def D(n):
    res = n*2 % 10000
    return res

#S명령어 수행하는 함수
def S(n):
    res = (n-1) % 10000 #음수의 mod연산
    return res

def bfs(s,e):
    visited = [0] * 10000
    queue = deque()
    queue.append([s,''])

    while queue:
        x, cnt = queue.popleft()

        if x == e:
            print(cnt)
            return
        
        #L명령어를 통한 값(tmp)를 방문하지 않았다면 방문하고, cnt에 L을 추가(L명령어를 썻다는 것을 기록)
        tmp = L(x)
        if visited[tmp]==0:
            visited[tmp] = 1
            queue.append([tmp,cnt+'L'])

        #R명령어를 통한 값(tmp)를 방문하지 않았다면 방문하고, cnt에 R을 추가(R명령어를 썻다는 것을 기록)
        tmp = R(x)
        if visited[tmp]==0:
            visited[tmp] = 1
            queue.append([tmp,cnt+'R'])

        #D명령어를 통한 값(tmp)를 방문하지 않았다면 방문하고, cnt에 D를 추가(D명령어를 썻다는 것을 기록)
        tmp = D(x)
        if visited[tmp]==0:
            visited[tmp] = 1
            queue.append([tmp,cnt+'D'])

        #S명령어를 통한 값(tmp)를 방문하지 않았다면 방문하고, cnt에 S를 추가(S명령어를 썻다는 것을 기록)
        tmp = S(x)
        if visited[tmp]==0:
            visited[tmp]=1
            queue.append([tmp,cnt+'S'])


t = int(input())
for _ in range(t):    
    s, e = map(int,input().split())
    bfs(s,e)