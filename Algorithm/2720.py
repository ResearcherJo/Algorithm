
money = [25,10,5,1]
count = [0,0,0,0]
t = int(input())

for i in range(t):
    m = int(input())
    
    if m>=money[0]:
        count[0]=m//money[0]
        m%=money[0]
    if m>=money[1]:
        count[1]=m//money[1]
        m%=money[1]
    if m>=money[2]:
        count[2]=m//money[2]
        m%=money[2]
    if m>=money[3]:
        count[3]=m//money[3]
        m%=money[3]
        
    print(count[0],count[1],count[2],count[3])
    count=[0,0,0,0]