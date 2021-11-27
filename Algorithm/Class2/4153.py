

while True:
    A, B, C = map(int,input().split())
    
    if A*B*C==0:
        break
    A, B, C = A*A, B*B, C*C
    if A==B+C or B==A+C or C==A+B:
        print('right')
    else:
        print('wrong')