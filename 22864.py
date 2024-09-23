

a, b, c, m = map(int,input().split())

p = 0
time = 24
w = 0

while time >0:
    if m>=p+a:
        w+=b
        time-=1
        p+=a
    else:
        time-=1
        p-=c
        if p<0:
            p=0
        
print(w)

'''
    while문의 작동 방식에 대해 조금 조심할 필요가 있으며 굳이 time을 변수로 잡지 않고, for문으로 그냥 24돌려도 됬다. time은 그저 24번의 연산 횟수일 뿐이다.

'''