from sys import stdin
from collections import deque

input= stdin.readline

a, b, c = map(int,input().split())

s = "0 "+"0 " + str(c) #처음 시작하는 c물통에만 물이 차있는 경우를 저장

arr = list() #조건에 맞을때 c에 있는 물의 양을 저장하는 list
visited= {s} #전에 만들어 졌는지 판단하는 visited
queue = deque()
queue.append(s)

def bfs(ma,mb,mc):
    

    while queue:
        #a, b, c에 각 물통에 들어있는 물의 양을 저장
        a, b, c = map(int,queue.popleft().split())

        #a에 들어있는 물의 양이 0이면 그때의 c를 arr에 추가
        if a==0:
            arr.append(c)

        #a물통에서 옮기는 경우
        if a!=0:
            #a에서 b로 옮기는 경우 
            if a+b<=mb:
                s = "0 " + str(a+b) + " " + str(c)
            else:
                s = str(a+b-mb) + " " + str(mb) + " " + str(c)
            
            if not (s in visited):
                visited.add(s)
                queue.append(s)

            #a에서 c로 옮기는 경우
            if a+c<=mc:
                s = "0 " + str(b) + " " + str(a+c)
            else:
                s = str(a+c-mc) + " " + str(b) + " " + str(mc)
            
            if not (s in visited):
                visited.add(s)
                queue.append(s)

        #b물통에서 옮기는 경우
        if b!=0:
            #b에서 a로 옮기는 경우
            if b+a<=ma:
                s = str(b+a) + " " + "0 " + str(c)
            else:
                s = str(ma) + " " + str(b+a-ma) + " " + str(c)
            
            if not (s in visited):
                visited.add(s)
                queue.append(s)

            #b에서 c로 옮기는 경우
            if b+c<=mc:
                s = str(a) + " " + "0 " + str(b+c)
            else:
                s = str(a) + " " + str(b+c-mc) + " " + str(mc)
            
            if not (s in visited):
                visited.add(s)
                queue.append(s)

        #c물통에서 옮기는 경우
        if c!=0:
            #c에서 a로 옮기는 경우
            if c+a<=ma:
                s = str(c+a) + " " + str(b) + " 0" 
            else:
                s = str(ma) + " " + str(b) + " " + str(c+a-ma)
            
            if not (s in visited):
                visited.add(s)
                queue.append(s)

            #c에서 b로 옮기는 경우
            if c+b<=mb:
                s = str(a) + " " + str(c+b) + " 0"
            else:
                s = str(a) + " " + str(mb) + " " + str(c+b-mb)
            
            if not (s in visited):
                visited.add(s)
                queue.append(s)


bfs(a,b,c)

arr.sort() #저장된 값을 오름차순으로 정렬

print(*arr)