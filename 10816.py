'''
풀이
https://velog.io/@babnbabn/10816번-숫자-카드-2-Python
'''
from sys import stdin

input = stdin.readline


def upperbound(array,n):
    start = 0
    end = len(array)-1

    while start<end:
        mid = (start+end)//2

        if n<array[mid]:
            end = mid
        else:
            start = mid+1
    if array[end]==n:
        return end+1
    return end

def lowerbound(array,n):
    start = 0
    end = len(array)-1

    while start<end:
        mid = (start+end)//2

        if n<=array[mid]:
            end = mid
        else:
            start = mid+1
    
    return end

n = int(input())
array = list(map(int,input().split()))
array.sort()#이분 탐색을 사용하기 위해서 값을 오름차순으로 정렬한다.
m = int(input())
li = list(map(int,input().split()))

for i in li:
    #print('upper : {}, lower : {}'.format(upperbound(array,i),lowerbound(array,i)))
    print(upperbound(array,i) - lowerbound(array,i),end=' ')

'''

dic = dict()
n = int(input())

array = list(map(int,input().split()))
for i in array: #상근이가 가지고 있는 카드들을 딕셔너리에 넣는다.
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

m = int(input())
li = list(map(int,input().split()))

for i in li:
    if i in dic: #확인할 카드가 dic에 있다면 1을 출력한다.
        print(dic[i],end=' ')
    else:#없다면 0을 출력한다.
        print(0, end=' ')
'''