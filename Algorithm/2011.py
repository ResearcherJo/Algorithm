from sys import stdin, stdout

input = stdin.readline 

array = [0] + list(input().strip())#dp[i-2]를 하기 위해서 하나 늘려준다.
dp = [0 for i in range(len(array))]

if int(array[1]) == 0: #array[1]이 0인 경우 암호가 될 수 없다.
    print("0")
    exit(0)

dp[0] = dp[1] = 1 # dp[i-2]를 하기 위해 dp[0]을 1로 초기화 해준다. array[1]은 0이아닌 경우 무조건 1이기에 dp[1] = 1이다.

for i in range(2,len(array)):
    one = int(array[i]) #1의 자리 
    ten = int(array[i-1])*10 + int(array[i]) #전 자리 까지 포함해서 계산한 10의 자리

    if one!=0 : 
        dp[i] += dp[i-1]
    if ten >= 10 and ten <=26 : #전 자리가 0 인 경우는 06과 같이 10보다 작기 때문에 고려해야 한다.
        dp[i] += dp[i-2]

print(dp[len(array)-1]%1000000)
