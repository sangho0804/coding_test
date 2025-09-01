import sys
input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
if N >= 0:
    is_prime[0] = False
if N >= 1:
    is_prime[1] = False

limit = int(N ** 0.5)
for p in range(2, limit + 1):
    if is_prime[p]:
        start = p * p
        step = p
        is_prime[start:N + 1:step] = [False] * (((N - start) // step) + 1)

out = []
append = out.append
for x in range(M, N + 1):
    if is_prime[x]:
        append(str(x))

sys.stdout.write("\n".join(out))
