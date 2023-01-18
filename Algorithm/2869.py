

A, B, V = map(int, input().split())

count=0
high = 0

count = (V-A)//(A-B)


V = V - count*(A-B)

#print(V)
if V-A<=0:
    count+=1
else:
    count+=2
print(count)