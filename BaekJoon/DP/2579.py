import sys
rd = sys.stdin.readline

n = int(rd().strip())
score = [0] + [int(rd()) for _ in range(n)]  # 1-index

# 작은 n 예외 처리
if n == 1:
    print(score[1])
    sys.exit(0)
if n == 2:
    print(score[1] + score[2])
    sys.exit(0)
if n == 3:
    print(max(score[1] + score[3], score[2] + score[3]))
    sys.exit(0)

dp = [0] * (n + 1)
dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[1] + score[3], score[2] + score[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + score[i],
                dp[i - 3] + score[i - 1] + score[i])

print(dp[n])