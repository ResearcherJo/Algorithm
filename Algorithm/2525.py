from sys import stdin, stdout

input = stdin.readline 


h = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

a, b = map(int,input().split())
p = int(input())

temp = (b+p)/60
b = (b+p)%60

a=h[int((a+temp)%24)]


print(a,b)