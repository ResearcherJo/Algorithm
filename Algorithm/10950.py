while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break
        
        
#예외처리의 중요성 sys.stdin을 써야하는건가