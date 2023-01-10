from sys import stdin

input = stdin.readline

number = int(input())

for i in range(number):
    n = int(input())

    array = [1 for i in range(n)]

    for j in range(3,n):
        array[j] = array[j-2]+array[j-3]
    
    print(array[n-1])