from sys import stdin

input = stdin.readline

N, K = map(int,input().split())
N_array = [int(input()) for _ in range(N)]
N_index = N-1
count = 0

while K!=0:
    if N_array[N_index] <= K:
        count += K // N_array[N_index] #K에 N_array[N_index]에 해당하는 돈을 얼마나 뺄 수 있는지 계산해서 더한다.
        K %= N_array[N_index] #K에 N_array[N_index]에 해당하는 돈을 얼마나 뺄 수 있는지 계산해서 뺀값을 K에 넣는다.
    else:
        N_index-=1

print(count)
