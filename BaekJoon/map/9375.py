import sys
from collections import Counter

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    kinds = Counter()
    for _ in range(n):
        name, kind = input().split()
        kinds[kind] += 1

    ans = 1
    for c in kinds.values():
        ans *= (c + 1)
    print(ans - 1)