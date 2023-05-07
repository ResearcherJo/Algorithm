from sys import stdin

input = stdin.readline

array = [list(map(int,input().split())) for _ in range(int(input()))]
count = 0#회의 횟수
fin = 0 #끝나는 시간

#빨리 끝나는 순으로 정렬
array.sort(key=lambda x : x[0])
array.sort(key=lambda x : x[1])

for key in array:
    #시작하는 시간이 끝나는 시간후라면 그 회의가 회의실을 사용한다. 끝나는 시간을 업데이트 한다.
    if key[0]>=fin:
        fin = key[1]
        count+=1
    
print(count)