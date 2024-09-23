
word = input().upper()
Alpha = dict()
for i in word:
    if Alpha.get(i):
        Alpha[i]+=1
    else:
        Alpha[i]=1
        
Alpha = Alpha.items()

Alpha = sorted(Alpha, key=lambda x : x[1],reverse=True)

if len(Alpha)>1:
    if Alpha[0][1]==Alpha[1][1]:
        print('?')
    else:
        print(Alpha[0][0])
else:
    print(Alpha[0][0])
        
