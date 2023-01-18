n = int(input())

count=0
number=666
while True:
    if count==n:
        break
    if '666' in str(number):
        count+=1
    number+=1


print(number-1)