'''
풀이
https://velog.io/@babnbabn/11279번-최대-힙
'''
from sys import stdin

input = stdin.readline

heap = [999] + list()


def heappush(n):
    heap.append(n)

    current = len(heap)-1 #가장 마지막 값의 index임

    while current>1:#부모가 있을 때까지
        if heap[current]>heap[current//2]:#current가 부모보다 크다면 부모랑 값을 바꾸자.
            heap[current], heap[current//2] = heap[current//2], heap[current]
            current//=2#부모를 current로 
        else:
            break
            
def heappop():
    if len(heap)==1: #비어있으니 그냥 0출력
        return '0'
    elif len(heap)==2: # heap에 1개밖에 없으니 출력하고 리턴
        return heap.pop()

    current = 1 # 1에서 부터 찾을 것이다.
    child = 2 #자식은 2부터 찾을 것이다.

    temp = heap[1]# root를 반환값으로 temp에 저장
    heap[current] = heap.pop() #root에 가장 마지막 값을 넣는다.

    while child<len(heap): #자식이 있다면 반복
        if child+1<len(heap) and heap[child]<heap[child+1]:#오른쪽 자식이 있고, 오른쪽 자식이 왼쪽 자식보다 크다면 오른쪽 자식을 가리키게
            child += 1
        if heap[current] < heap[child]:#current값이 자식 값보다 작다면 자식 값과 바꾸고, current가 자식을 바라보게 한다. child는 current의 자식을 본다.
            heap[current], heap[child] =heap[child], heap[current]
            current = child
            child *=2
        else:
            break

    return temp


n = int(input())

for i in range(n):
    x = int(input())
    if x:
        heappush(x)
    else:
        print(heappop())
    #print(*heap)
