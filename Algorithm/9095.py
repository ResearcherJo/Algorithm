

from sys import stdin, stdout

input = stdin.readline 

t = int(input())

array = [0 for i in range(12)]
array[1] = 1
array[2] = 2
array[3] = 4


for i in range(t) : 
    n = int(input())

    for j in range(4, n+1):
        array[j] = array[j-1] +array[j-2] +array[j-3]
        
    print(array[n])

