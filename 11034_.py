

import sys

count = 0

while True:
    try:
        a, b, c = map(int,sys.stdin.readline().split())    
        print(max(b-a,c-b)-1)
    except:
        break

    
        
'''
    그냥 답을 봐버렸다. 근데 내 아이디어는 브루트포스였다면 예는 수학적으로 생각했다... 정말 이런 느낌으로 풀기는 했었는데, 이렇게 수학으로 풀 수 있을지 모르겠다.
    그래서 문제를 보고 어떻게 풀 수 있을까 와 어떻게 표현할 수 있을까 그리고 내가 생각하는게 정확하게 뭔가를 정리해야 겠다.
    
    
    import sys

    count = 0

    lines = sys.stdin.readlines()
    for line in lines: 
        a, b, c = map(int,line.split())
        print(max(b-a,c-b)-1)
        
'''