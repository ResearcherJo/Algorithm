import sys
sys.setrecursionlimit(10**6) #충분한 재귀 깊이를 주어 오류를 예방
 
def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [False] * (N+1) #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            
    print(N - len(result)) #팀에 없는 사람 수

'''
from sys import stdin

input = stdin.readline

def cal(array, n):
    count = 0
    visit = [0] * (n+1)
    stack = list()

    for i in range(1, len(array)):
        if i == array[i]:
            visit[i] = 1

    for i in range(1,n+1):
        
        if not visit[i]:
            a = array[i]
            visit[i] = 1
            stack.append(i)
           
            while not visit[a]:
                stack.append(a)
                visit[a] = 1
                a = array[a]

            if a!=i:
                count+=1
                while stack:
                    visit[stack.pop()] = 0
            else:
                while stack:
                    stack.pop()
                

    return count


t = int(input())

for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))

    print(cal(array,n))
'''
    