from sys import stdin

input = stdin.readline

a, b = map(int,input().split())
m = int(input())
array = list(map(int,input().split()))

n = 0
#a진법의 수를 10진수로 변환한다.
array.reverse()#진법을 변환하려면 뒤에서 부터 읽어야 하기 때문에 reverse한다.
for i in range(m):
    n += array[i] * (a**i)

#10진법 n을 b진법으로 변환한다.
change = list()
while n!=0:
    change.append(n%b)
    n=n//b

print(*change)

