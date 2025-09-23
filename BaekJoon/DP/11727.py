'''
2xn

1x2 [a1], 2x1[b], 2x2 [a2]

a2 를 0 ~ n//2 개를 사용하는 경우
- a2 를 0 ~ (n- (n//2) // 2 개를 사용하는 경우


'''

import sys
import math
MOD = 10007

n = int(sys.stdin.readline())

cnt = 0

for i in range(0, n // 2 + 1):
    remain = n - 2 * i
    
    for j in range(0, remain // 2 + 1):
        k = remain - 2 * j
        block = i + j + k

        way = math.comb(block, k) * math.comb(block - k, j)
        cnt += way

print(cnt % MOD)


# # GPT code
import sys

MOD = 10007
n = int(sys.stdin.readline())

if n == 1:
    print(1)
else:
    a, b = 1, 3          
    for _ in range(3, n + 1):
        a, b = b, (b + 2 * a) % MOD
    print(b)