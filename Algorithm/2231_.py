

N = int(input())

for i in range(1,N+1):
    key = i
    hap = 0
    hap+=i
    while True:
        hap += i%10
        if i<10:
            break
        i = i//10
    if hap == N:
        print(key)
        break
else:
    print('0')
    
    
'''
    문제를 이해를 잘 못한거 같다. 아니 1같은 경우를 그냥 1이라고 생각 했는데 알고 보니 분해합은 자기자신+각 자리수 이어서 1+(1의자리수)1 = 2이었던거다. 
    문제를 좀 제대로 읽어야 겠다. 바로 되지는 않겠지만 노력해봐야겠다.
'''