 
    
    
a, b = map(int, input().split())    

if(b>a) : a,b = b,a
a1 = a
b1 = b

while(b!=0):
    a=a%b
    a,b=b,a

print(a)
print(a1*b1//a)

'''
    유클리드 호제법을 아느냐 마느냐의 문제여서 그냥 소스 가져왔다. 유클리드 호제법은 따로 이론으로 정리해야겠다. 거기에 a*b/최대공약수가 최소공배수라는 것도 알아야 했다.
'''