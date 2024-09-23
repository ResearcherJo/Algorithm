

import sys

l=list()

for i in range(9):
    l.append(int(sys.stdin.readline().strip()))
    

l.sort()    
for a in range(9):
    for b in range(a+1,9):
        for c in range(b+1,9):
            for d in range(c+1,9):
                for e in range(d+1,9):
                    for f in range(e+1,9):
                        for g in range(f+1,9):
                            
                            if l[a]+l[b]+l[c]+l[d]+l[e]+l[f]+l[g]==100:
                                print(l[a])
                                print(l[b])
                                print(l[c])
                                print(l[d])
                                print(l[e])
                                print(l[f])
                                print(l[g])
                                exit()
                
                
    '''
        아무거나 출력한다 면 그냥 출력하고 나가 버리자...
        
    '''