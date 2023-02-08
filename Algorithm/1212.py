from sys import stdin

input = stdin.readline

s = input().strip()

print(bin(int(s,8))[2:])


#다른 풀이
eight=input()

two = ["000", "001", "010", "011", "100", "101", "110", "111" ]

temp=0

for i in range(len(eight)):
    temp = int(eight[i])

    if i==0:
        print(int(two[temp]),end='')
    else:
        print(two[temp],end='')
