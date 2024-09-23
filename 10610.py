from sys import stdin

input = stdin.readline

n = list(input())
sum = 0
zero = False

#각자리수를 sum에다가 더하고, 0이 있는지 판단한다.
for i in range(len(n)-1):
    sum += int(n[i])
    if n[i]=='0':
        zero = True

#sum이 3의 배수이고, 0이 있다면 30의 배수가 될 수 있다는 소리이다.
if zero and sum%3==0:
    #내림차순으로 정렬해서 가장 큰 수를 만든다.
    n.sort(reverse=True)
    print(''.join(n))
else:
    print(-1)

