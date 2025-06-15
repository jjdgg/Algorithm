t = int(input())
dp = [[0, 0] for _ in range(41)]

# 초기값 설정
dp[0] = [1, 0]
dp[1] = [0, 1]

# DP 테이블 채우기
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

# 테스트 케이스 처리
for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])
