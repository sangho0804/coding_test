# my code 164 ms
import sys
from collections import deque
rd = sys.stdin.readline

N = int(rd())
arr = deque(i for i in range(N, 0 , -1))

while True:
    try:
        ans = arr.pop()
        x = arr.pop()
        arr.appendleft(x)
    except:
        break

print(ans)


# # gpt code 164 ms
# import sys
# from collections import deque

# rd = sys.stdin.readline
# N = int(rd())
# q = deque(range(1, N + 1))

# while len(q) > 1:
#     q.popleft()           # 버림
#     q.append(q.popleft()) # 다음 카드를 맨 뒤로

# print(q[0])