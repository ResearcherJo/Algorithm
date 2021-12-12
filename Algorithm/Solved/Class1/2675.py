

n = int(input())

for i in range(n):
    a, s = input().split()
    a = int(a)
    s = list(s)
    number = len(s)
    asd=''
    for j in range(number):
        ind = ''
        for k in range(a):
            ind += s[j]
        asd+=ind
    print(asd)
    
    
    ''' 좀 더 좋은 해결책
        n = int(input())
        
        for i in range(n):
            a, b = input().split()
            
            for j in b:
                print(int(a)*j,end='')
            print()    
    '''