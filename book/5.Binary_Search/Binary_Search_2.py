'''
    
    N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
    단, 이 문제의 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

    입력 예시
    7 2
    1 1 2 2 2 2 3

    출력 예시
    4
    
'''



import sys
from bisect import bisect_left,bisect_right

n, m = map(int,input().split())

l = list(map(int,sys.stdin.readline().split()))
         
print(bisect_right(l,m)-bisect_left(l,m))