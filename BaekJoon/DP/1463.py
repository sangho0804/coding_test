import sys
rd = sys.stdin.readline

N = int(rd())
dp = [0]*(N+1)  # dp[1]=0

for x in range(2, N+1):
    m = dp[x-1] + 1
    if x % 2 == 0:
        m = min(m, dp[x//2] + 1)
    if x % 3 == 0:
        m = min(m, dp[x//3] + 1)
    dp[x] = m

print(dp[N])