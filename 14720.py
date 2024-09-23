

n = int(input())
l = list(map(int,input().split()))

flag = -1
count=0

for i in l:
    if flag+1==i:
        flag+=1
        count+=1
        if flag==2:
            flag=-1
        
print(count)


'''

    n = int(input())
    l = list(map(int,input().split()))
    
    flag = -1
    count=0
    
    for i in l:
        if (flag+1)%3==i:
            flag+=1
            count+=1
    
            
    print(count)
    
    
    %3을 생각 했었다면 좀 더 편했으리 이게 0, 1, 2가 반복된다는 걸 보고 %3을 생각해 냈을 수 있을거같다.
'''