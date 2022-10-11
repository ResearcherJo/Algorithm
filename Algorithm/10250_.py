t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    
    num = n//h+1
    floor = n%h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    
    print(f'{floor*100+num}')
    
    '''
    
    진짜 생각을 못하겠음 나중에 밥 든든하게 먹고 다시 풀어볼거임
    
    '''