# # my code

# n = int(input())

# score = []

# for i in range(0, n):
#     plom = input().strip()
#     c_score = 0
#     add_score = 0
#     for idx, bol in enumerate(plom):
#         if bol == 'O':
#             add_score += 1
#             c_score += add_score
#         else :
#             add_score = 0
#     score.append(c_score)

# print(*score)


# gpt code 

import sys

rd = sys.stdin.readline
w = sys.stdout.write

n = int(rd())
out = []

for _ in range(n):
    s = rd().strip()
    run = 0      # 연속 'O' 길이
    total = 0    # 누적 점수
    for ch in s:
        if ch == 'O':
            run += 1
            total += run
        else:
            run = 0
    out.append(str(total))

w(" ".join(out))