



import sys 

s = sys.stdin.readline().strip()

c = len(s)
n = int(sys.stdin.readline().strip())

for i in range(n):
    m = sys.stdin.readline().strip()
    if m=='L' and c!=0: 
        c-=1
    elif m='D' and c!=len(s):
        c+=1
    elif m=='B':
        
        