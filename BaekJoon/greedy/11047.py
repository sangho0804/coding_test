# my code 36 ms 32412 kb
import sys
rd = sys.stdin.readline

N, K = map(int, rd().split())

wallet = []
for _ in range(N):
    coin = int(rd())
    wallet.append(coin)

wallet.sort(reverse=True)

ans = 0
for i in (wallet):
    div = K // i
    mod = K % i

    if div > 0:
        ans += div
        if mod == 0:
            break
        K = mod
        
print(ans)

# gpt code 32 ms 32544 kb
import sys

rd = sys.stdin.readline
N, K = map(int, rd().split())
coins = [int(rd()) for _ in range(N)]

cnt = 0
for a in reversed(coins):
    if a <= K:
        q = K // a
        cnt += q
        K -= q * a
        if K == 0:
            break

print(cnt)