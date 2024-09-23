from sys import stdin

input = stdin.readline

eight=input()

two = ["000", "001", "010", "011", "100", "101", "110", "111" ] # 8진수들을 2진수로 표현하는 경우의 수

temp=0

for i in range(len(eight)):
    temp = int(eight[i])

    if i==0:
        print(int(two[temp]),end='') #0이 아니면 0으로 시작하면 안되기때문에 int로 001 같은 것들을 1로 출력해준다.
    else:
        print(two[temp],end='')
