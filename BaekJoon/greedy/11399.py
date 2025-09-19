# my code 32412 kb, 48 ms
import sys
rd = sys.stdin.readline

N = int(rd())

time = list(map(int, rd().split()))

time.sort()

ans = time[0]
for p in range(2, N+1):
    pi = sum(time[:p])

    ans += pi

print(ans)

# gpt code 32412 kb, 36 ms
import sys
rd = sys.stdin.readline

N = int(rd())
P = list(map(int, rd().split()))
P.sort()

# 방법 1: 누적합
ans = 0
prefix = 0
for x in P:
    prefix += x
    ans += prefix
print(ans)