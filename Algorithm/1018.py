import sys


B = [['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B']]

W = [['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W'],
     ['W','B','W','B','W','B','W','B'],
     ['B','W','B','W','B','W','B','W']]


y, x = map(int,input().split()) 

s=list()

for i in range(y):
    s.append(list(sys.stdin.readline().strip()))

mn = 999
key = list()
for m in range(y-7):
    for i in range(x-7):
        count_b=0
        count_w=0
        s1 = [s[k][0+i:8+i] for k in range(0+m,8+m)]
        
        #print(s1)
        for k in range(8):            
            for j in range(8):     
                if B[k][j]!=s1[k][j]:
                    count_b+=1
                if W[k][j]!=s1[k][j]:
                    count_w+=1
        if min(count_w,count_b)<mn:
            mn = min(count_w,count_b)
        
    
print(mn)
                
