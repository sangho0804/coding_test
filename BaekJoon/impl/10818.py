# my code 644 ms

# import sys
# rd = sys.stdin.readline

# _ = int(rd())
# n = list(map(int, rd().split()))
# n = sorted(n)

# print(n[0], n[len(n)-1])


# gpt code 312 ms

import sys

rd = sys.stdin.readline

_ = rd() 
nums = list(map(int, rd().split()))

print(min(nums), max(nums))