from sys import stdin

input = stdin.readline

#수열 계산하는 함수
def cal(n,p):
    c = 0
    while(n!=0):
        c += (n%10)**p
        n//=10

    return c

a, p = map(int,input().split())

d = list()
d.append(a)

while(1):
    n = cal(d[-1],p)

    if n in d: #다음 항(n)이 수열에 있다면 n의 index를 출력한다.
        i = d.index(n)
        print(i)
        break
    else: #n이 수열에 없다면 수열에 추가한다.
        d.append(n)
