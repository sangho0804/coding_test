# my code 

# import sys
# rd = sys.stdin.readline

# n = int(rd())

# # 신청자의 수 $S, M, L, XL, XXL, XXXL 6종류

# size = list(map(int, rd().split()))

# T, P = map(int, rd().split())

# count_t = 0

# for i in size:
#     if i > T :
#         count_t += (i // T)
#         i = i % T

#     if i > 0 and i <= T:
#         count_t += 1
            

# print(count_t)
# print(n // P, n % P)


# gpt code 

import sys

rd = sys.stdin.readline

N = int(rd().strip())
sizes = list(map(int, rd().split()))  # S, M, L, XL, XXL, XXXL
T, P = map(int, rd().split())

# 1) 티셔츠 묶음 수 (각 사이즈별 올림 후 합)
tshirt_bundles = sum((x + T - 1) // T for x in sizes)

# 2) 펜: P묶음을 최대화하고, 남은 건 낱개로
pen_bundles = N // P
pen_singles = N % P

print(tshirt_bundles)
print(pen_bundles, pen_singles)