'''
    -를 보면 뒤를 확인 한다. 뒤에 나오는 연산자가 +라면 먼저 실행하고, -라면 앞의 -를 먼저 실행한다.
    뒤에 나오는 연산자가 +라면 그 뒤로 계속 계산해 본다. 언제까지? -가 나오거나, 끝날때 까지

'''

from sys import stdin

input = stdin.readline

s = input()
s_n = list(map(int,s.replace('+','-').split('-')))
count = 0
o = -1
m = 0

for i in range(len(s)):
    if s[i] =='+' or s[i] == '-':
        count += 1
    if s[i] == '-':
        m+=1
        if o != -1:
            n1 = s_n.pop(o-1)
            n2 = s_n.pop(o-1)
            #print('n1',n1,'n2',n2)
            n = n1 - n2
            s_n.insert(o-1,n)
            #print(count,*s_n)
            count -= 1
            m-=1
        o = count
    if s[i] == '+' and o!=-1:
        n1 = s_n.pop(o)
        n2 = s_n.pop(o)

        n = n1 + n2
        count -= 1
        s_n.insert(o,n)
    
#print(*s_n)
if m:
    n1 = s_n.pop(o-1)
    n2 = s_n.pop(o-1)
    n = n1 - n2
    count -= 1
    s_n.insert(o-1,n)

sum = 0
for i in s_n:
    sum+=i

print(sum)


'''
반례
1-2-3+4 / -8
1000 / 1000
1-1-1 / -1
1+2-3+4+5 / -9
1-1  답: 0 
1+2-3+4+5 답: -9
10-10+10-10+10  답: -30
50-60+60+70+70-50 답: -260
1+2+3+7+8 답: 21
00000-1+00000-00005 답: -6
'''