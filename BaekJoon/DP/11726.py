# my code 34668kb	52ms
import sys
import math
rd = sys.stdin.readline


N = int(rd().strip())

y = 2 * N
cnt = 0

if y % 2 == 0 :
    cnt += 1

for i in range(1, y//4+1):

    _case = y - (4 * i)
    quot = _case//2
    test = [0] *(i + quot)

    num = math.comb(len(test), i)
    cnt += num

print(cnt%10007)

# refactoring my code 34536kb	48ms
import sys
import math

MOD = 10007
n = int(sys.stdin.readline())

total = 0
for h in range(0, n // 2 + 1):           # h: 가로 쌍(2x2) 개수
    total = (total + math.comb(n - h, h))

print(total % MOD)


# gpt code 32544kb	36ms
import sys

MOD = 10007
n = int(sys.stdin.readline())

if n == 1:
    print(1)
else:
    a, b = 1, 2        # a=dp[1], b=dp[2]
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD
    print(b % MOD)