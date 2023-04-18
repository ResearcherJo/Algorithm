'''
풀이
https://velog.io/@babnbabn/10815번-숫자-카드-Python
'''
from sys import stdin

input = stdin.readline
'''
def find(array, n):
    #초기 값을 array의 인덱스로 초기화 한다.
    start = 0 # 가장 작은 인덱스
    end = len(array)-1 #가장 큰 인덱스

    while start<=end:
        mid = (start+end)//2 #인덱스의 중간값
        if array[mid]>n: #찾으려고 하는 값(n)이 array[mid]보다 작다면 mid뒤쪽에는 값이 없기 때문에 end를 mid-1로 바꾼다.
            end = mid-1
        elif array[mid]<n: #찾으려고 하는 값(n)이 array[mid]보다 크다면 mid앞쪽에는 값이 없기 때문에 start를 mid+1로 바꾼다.
            start = mid+1
        else: # array[mid]와 찾으려고 하는 값(n)이 같다면 1을 리턴한다.
            return 1
        
    return 0 #while문을 돌면서 1을 리턴하지 않았다는 것은 없다는 것이기에 0 리턴


n = int(input())
array = list(map(int,input().split()))
array.sort()#이분 탐색을 사용하기 위해서 값을 오름차순으로 정렬한다.
m = int(input())
li = list(map(int,input().split()))

for i in li:
    print(find(array,i),end=' ')
'''

dic = dict()
n = int(input())

array = list(map(int,input().split()))
for i in array: #상근이가 가지고 있는 카드들을 딕셔너리에 넣는다.
    dic[i] = 0

m = int(input())
li = list(map(int,input().split()))

for i in li:
    if i in dic: #확인할 카드가 dic에 있다면 1을 출력한다.
        print(1,end=' ')
    else:#없다면 0을 출력한다.
        print(0, end=' ')