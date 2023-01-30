from sys import stdin

input = stdin.readline

S = input()

for i in S:
    if i.islower():
        print(chr(97+(ord(i)+13-97)%26), end = '') #z의 값을 넘으면 a로 돌아가서 계산할 수 있도록 하는 계산
    elif i.isupper():
        print(chr(65+(ord(i)+13-65)%26), end = '') #Z의 값을 넘으면 A로 돌아가서 계산할 수 있도록 하는 계산
    else:
        print(i, end = '')