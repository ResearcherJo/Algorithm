




n = int(input())
s=1

for i in range(1,n+1):
    s*=i

count=0

while s%10==0:
    if s%10==0:
        count+=1
        s//=10
    else:
        break
        
print(count)

'''
    OverflowError가 나면 최대 경우의 수를 입력해보고 읽어보자. 우선 이 문제에서는 /=를 쓰면 float으로 되고, float은 최대수가 작아서 Error가 났던 거다
'''