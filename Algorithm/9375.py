from sys import stdin

input = stdin.readline

t = int(input()) #테스트케이스 입력

for _ in range(t):
    n = int(input())
    dic = dict()
    for i in range(n):
        c, ty = input().split()
        if ty in dic: #입력받은 옷의 종류가 있는 종류라면 +1을 한다.
            dic[ty] += 1
        else: #입력받은 옷의 종류가 없는 종류라면 2로 저장한다. (옷의 개수 1 + 선택안할경우 1)
            dic[ty] = 2
    
    sum =1
    for j in dic:
        sum *= dic[j]

    print(sum-1)

