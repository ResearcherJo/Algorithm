
import sys

n, m = map(int,input().split())

l=dict()
count = 0
g = list()

for i in range(n+m):
    s = sys.stdin.readline().strip()
    if l.get(s,0)!=0:
        g.append(s)
        count+=1        
    else:
        l[s]=1
        
print(count)
g.sort(key = lambda x:x[0])
for i in g:
    print(i)
    
'''

    # BOJ 1764 - 듣보잡
    import sys
    
    N, M = map(int, sys.stdin.readline().split())
    N_list = [sys.stdin.readline().strip() for i in range(N)]
    M_list = [sys.stdin.readline().strip() for i in range(M)]
    
    # 교차하는 이름들을 찾는다
    duplicate = list(set(N_list) & set(M_list))
    
    print(len(duplicate))
    for name in sorted(duplicate):
        print(name)
        
    집합을 이용하면 좀 더 빠르게 해결할 수 있었떤 문제였다. 두개의 값을 비교하는 거였으니까 교집합을 구하면 됬다.

'''