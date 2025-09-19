# my code 51480 kb, 164 ms
import sys
rd = sys.stdin.readline
w = sys.stdout.write

N, M = map(int, rd().split())

memo = {}
for _ in range(N):
    site, pss = rd().split()
    memo[site] = pss

ans = []
for _ in range(M):
    search = rd().strip()
    ans.append(memo.get(search))

w('\n'.join(ans))    


# gpt code  51480 kb, 164 ms
import sys
rd = sys.stdin.readline

N, M = map(int, rd().split())
pw = {}

for _ in range(N):
    site, p = rd().split()
    pw[site] = p

out = []
for _ in range(M):
    q = rd().strip()
    out.append(pw[q])

print("\n".join(out))