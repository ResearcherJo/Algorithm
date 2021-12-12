

n = int(input())


l = list()
for i in range(n):
    st = input()
    l.clear()
    count = 0
    for j in st:
        if j=='O':
            l.append('O')
        else:
            l.clear()
        count+=len(l)
    print(count)
    
    
'''좀 더 쉬운 코드
    import sys

    n = int(sys.stdin.readline())
    
    for i in range(n):
        ox = sys.stdin.readline()
        oc = 0
        oc_t = 0
        
        for j in range(len(ox)):
            
            if ox[j] == 'O':
                oc += 1            
            else:
                oc = 0
                
            oc_t += oc
            
        print(oc_t)
'''