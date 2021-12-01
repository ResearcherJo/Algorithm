

T = int(input())

time=[300,60,10]

count=[0,0,0]

if T>=time[0]:
    count[0] = T//time[0]
    T%=time[0]
if T>=time[1]:
    count[1] = T//time[1]
    T%=time[1]
if T>=time[2]:
    count[2] = T//time[2]
    T%=time[2]
if T==0:
    print(count[0],count[1],count[2])
else:
    print('-1')
    