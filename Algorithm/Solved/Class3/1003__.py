zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())
    
for _ in range(T):
    fibonacci(int(input()))
    
    
'''
    그냥 야예 아이디어 조차 얻지 못했으며 f(n)일 때 호출되는 f(0)과 f(1)의 횟수는 f(n-1)일때 호출되는 수 + f(n-2)일때 호축되는 수 임을 몰랐다.
    그저 f(n)=f(n-1)+f(n-2)임을 보고 알아냈어야 했다...
'''