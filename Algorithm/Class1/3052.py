
l = list()

count=0

for i in range(10):
    n = int(input())
    if n%42 not in l:
        l.append(n%42)
        count+=1
print(count)