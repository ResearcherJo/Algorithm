from sys import stdin

input = stdin.readline

S = input().strip() #len함수가 문자열 끝의 '\n'까지 세기 때문에 제거해줘야 한다.
print(len(S))