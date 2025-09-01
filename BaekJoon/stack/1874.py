import sys
from collections import deque
rd = sys.stdin.readline

n = int(rd())
target = [int(rd()) for _ in range(n)]

stack = []
ops = []
next_push = 1

for x in target:
    while next_push <= x:
        stack.append(next_push)
        ops.append('+')
        next_push += 1

    # 꼭대기가 x면 pop
    if stack and stack[-1] == x:
        stack.pop()
        ops.append('-')
    else:
        print("NO")
        sys.exit(0)

print('\n'.join(ops))

