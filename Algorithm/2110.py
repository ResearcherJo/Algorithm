'''
풀이
https://velog.io/@babnbabn/2110번-공유기-설치-Python
'''
from sys import stdin

input = stdin.readline

def find(array,c):

    #start를 가장 작은 간격, end를 가장 큰 간격으로 초기화 하낟.
    start = 1
    end = array[-1] - array[0]

    while start<=end:
        count = 1

        mid = (start+end)//2
        current = array[0] #마지막으로 공유기를 놓은 곳을 저장 / 첫번째 집에는 공유기를 놓는다.

        for i in array:
            if i>=mid+current: #마지막에 공유기 놓은 곳에서 mid만큼 떨어진 곳보다 뒤에 있다면 공유기를 놓는다.
                current = i
                count+=1

        if count>=c:#mid의 간격으로 공유기를 놓을 수 있다면 간격(mid)를 늘려보자
            start = mid+1
        else:#공유기를 못 놓는 다면 간격(mid)를 줄여보자.
            end = mid-1

    return end

n, c = map(int,input().split())
array = [int(input())for _ in range(n)]

array.sort() #집들이 순서대로 들어가 있게 정렬

print(find(array,c))