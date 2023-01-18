from sys import stdin, stdout

input = stdin.readline 

n = int(input())

array = [0 for i in range(10000)]

array[1] = 1
array[2] = 2

for i in range(3, n+1):
    array[i] = array[i-1]+array[i-2]

print(array[n]%10007)
