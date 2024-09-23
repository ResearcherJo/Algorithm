'''
풀이
https://velog.io/@babnbabn/1780번-종이의-개수-Python
'''
import sys
sys.setrecursionlimit(10**6) #제귀함수 제한 안걸리게 하는 것

input = sys.stdin.readline

count = {-1:0,0:0,1:0} #해당하는 숫자 카운트

def div(array, n,x,y):
    
    flag = array[y][x] #처음자리에 저장되어 있는 숫자

    for i in range(y,y+n):
        for j in range(x,x+n):
            if array[i][j] != flag: #처음숫자(flag)와 다르다면 사용할 수 없는 종이니까 잘라야 한다.
                next=n//3
                div(array,next,x+(next*0),y+(next*0)) #1번째
                div(array,next,x+(next*1),y+(next*0)) #2번째
                div(array,next,x+(next*2),y+(next*0)) #3번째
                div(array,next,x+(next*0),y+(next*1)) #4번째
                div(array,next,x+(next*1),y+(next*1)) #5번째
                div(array,next,x+(next*2),y+(next*1)) #6번째
                div(array,next,x+(next*0),y+(next*2)) #7번째
                div(array,next,x+(next*1),y+(next*2)) #8번째
                div(array,next,x+(next*2),y+(next*2)) #9번째
                return #9개로 자른거 다 봤으면 나가야함 안나가면 result를 증가시킴
            
    count[flag]+=1 #for문을 그냥 통과했다는건 모두 숫자가 같다는 소리니까 해당하는 숫자 count
    return#다했으니 return


n = int(input())
array = [list(map(int,input().split()))for _ in range(n)]

div(array,n,0,0)

for i in count.values():
    print(i)