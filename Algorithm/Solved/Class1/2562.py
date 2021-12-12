
a = list()

for i in range(9):
    
    a.append(int(input()))
    
m = max(a)    
for i in range(len(a)):
    if a[i]==m:
        print(m)
        print(i+1)
        break
    