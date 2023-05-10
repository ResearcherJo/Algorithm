from sys import stdin
 
input = stdin.readline

N = int(input())
sum = 0
marr = list() #음수를 가지는 리스트
parr = list() #양수를 가지는 리스트

for _ in range(N):
    n = int(input())
    #1의 경우는 더하는 것 밖에 없다.
    if n==1:
        sum += 1
    #0초과면 parr에 넣는다.
    elif n>0:
        parr.append(n)
    #0이하면 marr에 넣는다.
    else:
        marr.append(n)


marr.sort(reverse=True) #내림차순 정렬
parr.sort() #오름차순 정렬

while parr:
    if len(parr)==1:#하나만 남는다면 그냥 더해라
        sum+=parr.pop()
    else: #양수들은 큰것들끼리 곱해서 더한다.
        sum+= parr.pop()*parr.pop()

while marr:
    if len(marr)==1:#하나만 남는다면 그냥 더해라.
        sum+=marr.pop()
    else:#음수는 작은 것들끼리 곱해서 더한다. 0은 남아있는 음수랑 곱해서 넣는다.
        sum+=marr.pop()*marr.pop()

print(sum)
