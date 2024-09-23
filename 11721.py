

s = input()

i=0
n=1
while i<len(s):
    if 10*n<=len(s):
        print(s[i:10*n])
    else:
        break
    i=10*n
    n+=1
if i!=len(s):        
    print(s[i:len(s)])
