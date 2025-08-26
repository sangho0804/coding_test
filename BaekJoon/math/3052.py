# 중복 제거 -> set -> unique (순서 무시)

import sys
rd = sys.stdin.readline
w = sys.stdout.write

ck = []
for _ in range(10):
    n = int(rd())
    ck.append(n%42)


unique = list(set(ck))

print(len(unique))