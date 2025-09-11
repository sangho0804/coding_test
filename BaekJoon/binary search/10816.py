# Counter 580 ms
import sys
from collections import Counter

rd = sys.stdin.readline
w = sys.stdout.write

N = int(rd())
cards = list(map(int, rd().split()))
M = int(rd())
queries = list(map(int, rd().split()))

count = Counter(cards) 

w(" ".join(str(count.get(x, 0)) for x in queries))


# # binary search 1276 ms
# import sys
# import bisect

# rd = sys.stdin.readline
# w = sys.stdout.write

# N = int(rd())
# cards = sorted(map(int, rd().split()))  # 정렬
# M = int(rd())
# queries = list(map(int, rd().split()))

# # print(cards)

# ans = []
# for x in queries:
#     # print('x : ', x)
#     left = bisect.bisect_left(cards, x)
#     # print('left :', left)
#     right = bisect.bisect_right(cards, x)
#     # print('right :', right)
#     ans.append(str(right - left))

# w(" ".join(ans))







