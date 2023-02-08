from sys import stdin

input = stdin.readline

n = int(input())
result =''
print(7//-2,7%-2)
while n!=0:
    if n%(-2): 
        result = '1' + result #-2로 나누어 떨어지지 않으니 1을 추가한다.
        n = n//-2+1 #-2로 나누어 떨어지지 않는경우 나머지가 -1이 아닌 1이 되게 하려먼 목을 하나 더해줘야 한다.
    else:
        result = '0' + result #-2로 나누어 떨어지니 0을 추가한다.
        n = n//-2

if not result: #n이 0이어서 result에 아무것도 없다면 0을 출력해야 한다.
    result = '0'    

print(''.join(result))