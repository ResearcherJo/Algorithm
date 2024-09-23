'''
풀이
https://velog.io/@babnbabn/1541번-잃어버린-괄호-Python
'''

from sys import stdin

input = stdin.readline

s = input()
s_n = list(map(int,s.replace('+','-').split('-')))
count = 0 #몇번째 연산자 까지 읽었는지 계산
o = -1
m = 0 #-의 개수를 저장

for i in range(len(s)):
    if s[i] =='+' or s[i] == '-':
        count += 1
    if s[i] == '-':
        m+=1
        if o != -1:
            n1 = s_n.pop(o-1)
            n2 = s_n.pop(o-1)
            n = n1 - n2
            s_n.insert(o-1,n)
            count -= 1
            m-=1
        o = count
    if s[i] == '+' and o!=-1: #지금 +인데, 앞에 -가 있다면
        n1 = s_n.pop(o)
        n2 = s_n.pop(o)
        n = n1 + n2
        count -= 1 #연산을 했으니 남은 연산자가 하나 줄었다.
        s_n.insert(o,n)
    

if m: #-가 남아있을 경우 계산해준다.
    n1 = s_n.pop(o-1)
    n2 = s_n.pop(o-1)
    n = n1 - n2
    count -= 1
    s_n.insert(o-1,n)

sum = 0#계산이 끝나고 나머지 들은 +들일 것이다. 다 더한다.
for i in s_n:
    sum+=i

print(sum)
