from sys import stdin

input = stdin.readline

n, k = map(int,input().split())

queue = [i+1 for i in range(n)]
array = list()

cnt = 0


for i in range(n):
    cnt = (cnt + k - 1)%len(queue)

    array.append(str(queue.pop(cnt)))

print("<",", ".join(array),">",sep='')