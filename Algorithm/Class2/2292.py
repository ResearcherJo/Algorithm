

N = int(input())


if N!=1:
    last = 1
    for i in range(1,N):
        #print((1+(6*(i-1))+1),(last+6*i))
        if (1+(6*(i-1))+1)<=N and (last+6*i)>=N:
            print(i+1)
            break
        last = last+6*i
    
else:
    print('0')
    '''
for j in range(1,7):
                if (3+(6*(i-1)))+(j*i)==N:
                    print(i)
                    break;
            else:
                print(i+1)
    '''