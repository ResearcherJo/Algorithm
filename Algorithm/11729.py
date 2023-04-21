import sys

input = sys.stdin.readline

def hannoi(n,f,w,to):
    global count
    if n==0:
        return
    else:
        hannoi(n-1,f,to,w)
        li.append((f,to))
        count+=1
        hannoi(n-1,w,f,to)

n = int(input())
li = list()
count=0
hannoi(n,1,2,3)
print(count)
for i in li:
    print('{} {}'.format(i[0],i[1]))