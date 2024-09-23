'''
풀이
https://velog.io/@babnbabn/2805번-나무-자르기-Python
'''
from sys import stdin

input = stdin.readline

def find(array, n):

    #초기값을 설정해준다.
    start = 1
    end = max(array)

    while start<=end:
        sum = 0
        mid = (start+end)//2

        for i in array:
            if i>mid: #자를 수 있다면
                sum+= i- mid #잘라서 sum에 더한다.

        if sum>=n:#sum이 조건을 충족한다면
            start = mid+1#좀 더 절단기를 높여서 찾아본다.
        else:#조건에 충족하지 못하면
            end = mid-1#좀 더 절달기를 낮춰서 찾아본다.
    
    #while문을 다 돌고 나면 end는 가장 최적의 값을 가지고 있다. 
    return end #end가 절단기의 최댓값을 가진다.


n, m = map(int,input().split())
array = list(map(int,input().split()))

print(find(array,m))