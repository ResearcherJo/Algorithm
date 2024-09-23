from sys import stdin

input = stdin.readline


while True:
    low = 0
    upp = 0
    num = 0
    voi = 0
    line = input().rstrip('\n') #문자열 뒤의 \n만 지우기 위함이다.

    if not line: # readline은 아무것도 입력되지 않았을때 EOFError가 아닌 빈 문자열을 반환한다.
        break

    for i in line:
        if i.islower():
            low+=1
        elif i.isupper():
            upp +=1
        elif i.isdigit():
            num +=1
        elif i.isspace():
            voi +=1
    print(low,upp,num,voi)