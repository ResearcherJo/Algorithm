

n = int(input())

l = list()
g = list()
for i in range(n+1):
    l.append(i)

for i in range(n//2):
    for j in range(i,len(l),2):
        if i*j<len(l):
            l[i*j]=0
        
    print(l)
    
    

for i in l:
    if i!=0:
        print(i)
    
'''

    n = int(input())
    arr = [i+1 for i in range(n)]
    tmp = []
    while len(arr) != 1:
        for idx, item in enumerate(arr):
            if idx % 2:
                tmp.append(item)
        arr = tmp
        tmp = []
    print(arr[0])
    
    처음 생각 했던 방식이었는데 메모리 때문에 안될줄 알았는데 그냥 할걸 그랬다. 긜고 enumerate도 좀 알아봐야 겠다. 
    사실 필요 없을지도? 그냥 굳이 삭제가 아니라 옮기면 된다는 아이디어를 가지고 있고, 구현할 줄 알았다면...

'''