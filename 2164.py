from collections import deque

N = int(input())

d = deque(i for i in range(1,N+1))

while len(d)!=1:
    d.popleft()
    d.append(d.popleft())
print(d[0])
    
'''
    아이디어는 맞았는데 pop이라는 함수는 사용이 안되고 사용 안하니 시간초과가 났다. 그래서 from collections import deque이거 찾아서 씀 굿
    https://mong9data.tistory.com/50여기서
'''