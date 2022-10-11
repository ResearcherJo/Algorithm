

n = int(input())
seat = list(input())

count = 1

i=0

while i<len(seat):
    if seat[i]=='S':
        count+=1
        i+=1
    elif seat[i]=='L':
        count+=1
        i+=2
    

if count>n:
    print(n)
else:
    print(count)
    
