import sys
rd = sys.stdin.readline
w = sys.stdout.write

N, M = map(int, rd().split())
arr = list(map(int, rd().split()))

prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# for i, v in enumerate(arr, 1):
#     prefix_sum[i] = prefix_sum[i - 1] + v
out = []
for _ in range(M):
    i, j = map(int, rd().split())
    out.append(str(prefix_sum[j] - prefix_sum[i - 1]))
    # print(prefix_sum[j] - prefix_sum[i - 1])

w("\n".join(out))


import sys
rd = sys.stdin.readline
w = sys.stdout.write

N, M = map(int, rd().split())
A = list(map(int, rd().split()))

# 누적합 (prefix[i] = A[0] ~ A[i-1] 합)
prefix = [0] * (N + 1)
for i, v in enumerate(A, 1):
    prefix[i] = prefix[i - 1] + v


out = []
for _ in range(M):
    i, j = map(int, rd().split())
    out.append(str(prefix[j] - prefix[i - 1]))

w("\n".join(out))