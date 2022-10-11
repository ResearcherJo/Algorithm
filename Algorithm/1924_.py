


day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

m=1
d=1
count=1

im, idd = map(int,input().split())

while True:
    
    
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if d==31:
            m+=1
            d=1
            count+=1
        else:
            d+=1
            count+=1
    elif m==2:
        if d==28:
            m+=1
            d=1
            count+=1
        else:
            d+=1
            count+=1
    elif m==4 or m==6 or m==9 or m==11:
        if d==30:
            m+=1
            d=1
            count+=1
        else:
            d+=1
            count+=1
    
    if im==m and d==idd:
        print(day[count%7])
        break
        
        
'''
    좀 더 간단하게 계살 할 방법을 찾지 않으면 시간초과가 난다. 
    이건 월을 그냥 31,30,28 이렇게 보고 일에 더하고 나눠서 요일을 구한다.

    Day = 0
    arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
     
    x, y = map(int,input().split())
     
    for i in range(x-1):
        Day = Day + arrList[i]
    Day = (Day + y) % 7
 
    print(weekList[Day])
'''