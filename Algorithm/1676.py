from sys import stdin

iniput = stdin.readline

n = int(input())

s=1
#n!을 구하는 반복문
for i in range(1,n+1):
    s*=i

count=0

#뒤의 0의 개수는 10으로 나눴을때 몇번 나눠 떨어지나와 같다.
while s%10==0:
    if s%10==0:
        count+=1
        s//=10
        #/=으로 하면 들어갈 수 있는 최대값이 작은 float이 되어서 오류가 날 수 있다.
    else:
        break
        
print(count)

'''
    OverflowError가 나면 최대 경우의 수를 입력해보고 읽어보자. 우선 이 문제에서는 /=를 쓰면 float으로 되고, float은 최대수가 작아서 Error가 났던 거다
'''