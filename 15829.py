

N = int(input())

S = list(input())


sum1 = 0

for i in range(N):
    sum1+=(ord(S[i])-96)*(31**i)
    

print(sum1%1234567891)

'''
 처음 50점이 나왔는데 그건 바로 문제를 제대로 읽지 않고  mod 1234567891을 안해줘서 그런거다. 문제좀 잘 읽자...
'''