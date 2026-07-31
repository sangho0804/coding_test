import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    digits = set()
    i = 1
    while True:
        num = N * i
        digits.update(str(num))
        if len(digits) == 10:
            break
        i += 1

    print(f'#{_ + 1} {num}')