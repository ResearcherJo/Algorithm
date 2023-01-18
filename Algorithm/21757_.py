import sys

# 재귀깊이해제
sys.setrecursionlimit(200000)

# go : 현재 idx번째 인덱스이고 경계선이 cnt개일 때 유효한 분할의 갯수를 리턴하는 함수
def go(idx, cnt):
    # Base Case : 경계선이 3개인 경우
    if cnt == 3:
        # 유효한 경계선인 경우
        if idx <= n - 1:
            return 1
        # 3개를 그엇으나 실질적으로 범위밖에서 그어 유효 경계선이 2개인 경우
        return 0
    # 범위를 벗어나는 경우
    if idx == n:
        return 0
    # Memoization
    if dp[idx][cnt] != -1:
        return dp[idx][cnt]
    dp[idx][cnt] = 0
    
    # 점화식
    if pf[idx] == (cnt + 1) * k:
        dp[idx][cnt] += go(idx + 1, cnt + 1)
    dp[idx][cnt] += go(idx + 1, cnt)
    
    return dp[idx][cnt]

# 입력부
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 누적합 계산
pf = [0] * n
pf[0] = arr[0]
for i in range(1, n):
    pf[i] = pf[i - 1] + arr[i]
    
# 합이 4의 배수가 아닌 경우
if pf[-1] % 4 != 0:
    print(0)
    
# 합이 4의 배수인 경우
else:
    k = pf[-1] // 4
    # dp : 현재 idx번째 인덱스이고 경계선을 cnt개만큼 그엇을 때 가능한 경우의 수를 저장하는 2차원 상태공간 배열
    dp = [[-1] * 4 for _ in range(n)]
    print(go(0, 0))
    print(dp)