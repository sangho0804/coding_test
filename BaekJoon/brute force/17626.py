import sys
import math
rd = sys.stdin.readline

n = int(rd().strip())


# depth 가 최소가 되는 


def is_square(x: int) -> bool:
    r = int(math.isqrt(x))
    return r * r == x

if is_square(n):
    print(1)
    raise SystemExit


limit = int(math.isqrt(n))
for a in range(1, limit + 1):
    if is_square(n - a * a):
        print(2)
        raise SystemExit
    
m = n
while m % 4 == 0:
    m //= 4

if m % 8 == 7:
    print(4)
else:
    print(3)