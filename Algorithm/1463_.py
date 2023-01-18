from sys import stdin, stdout

input = stdin.readline 


array = [ 0 for i in range(1000001)]

array[1] = 0

n = int(input())

for i in range(2,n+1):
    if i%3==0 and i%2==0 : 
        array[i] = min(array[i-1], array[i//3], array[i//2]) + 1
    elif i%3==0 : 
        array[i] = min(array[i-1], array[i//3]) + 1
    elif i%2==0 :
        array[i] = min(array[i-1], array[i//2]) +1
    else :
        array[i] = array[i-1]+1

print(array[n])


'''
    3과 2의 공배수는 따로 처리해줘야 한다.
'''