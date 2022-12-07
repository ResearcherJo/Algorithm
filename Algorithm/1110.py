from sys import stdin, stdout

input = stdin.readline 

count = 0
n = int(input().rstrip())
tmp = n

while(1) : 
    if n<10 :
        n = n + n*10
    else:
        n = ((n%10)*10) + ((n%10 + n//10)%10)

    count +=  1

    if tmp == n:
        print(count)
        break
