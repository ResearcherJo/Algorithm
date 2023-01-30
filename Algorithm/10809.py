from sys import stdin

input = stdin.readline

S = input()

array = [-1 for i in range(26)] # 포함되어 있지 않은 경우 -1이기에 -1로 초기와

for i in range(26):
    s = chr(i+97) #a ~ z까지 비교하기 위함이다.
    if s in S:
        array[i] = S.index(s) 

print(*array)