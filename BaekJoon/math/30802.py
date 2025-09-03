import sys
rd = sys.stdin.readline

n = int(rd())

# 신청자의 수 $S, M, L, XL, XXL, XXXL 6종류

size = list(map(int, rd().split()))

T, P = map(int, rd().split())

count_t = 0

for i in (size):
    if i > 5 :
        count_t += (i // 5)
        i = i % 5

    if i > 0 and i <= 5:
        count_t += 1
            

print(count_t)
print(n // P, n % P)