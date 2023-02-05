'''
2개의 자연수 또는 정식(整式)의 최대공약수를 구하는 알고리즘의 하나이다.
호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
0의 약수는 모든 자연수이다.

두 자연수의 곱 = 최대공약수 * 최소공배수
'''

def gcd(a, b):
    if(b>a) : a,b = b,a

    while(b!=0):
        a=a%b
        a,b=b,a
        
    return a


def gcd(a, b):
    
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)


