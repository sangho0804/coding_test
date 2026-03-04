# my code
# a + b + c  + abc = N

# Problem 1: Iterates over the entire range unnecessarily.
# Problem 2: Recreates a digit list every iteration.
# Problem 3: Does not break after finding a valid constructor.
# Problem 4: Saves the digit string instead of the constructor value.

import sys
input = sys.stdin.readline

N = int(input())
result = 0
for i in range(N-1, 0, -1):
    st = str(i)
    arr = []
    for j in st:
        arr.append(int(j))

    ans = sum(arr) + i
    if N == ans :
        result = "".join(str(n) for n in arr)
print(result)


# gpt code
import sys
input = sys.stdin.readline

N = int(input())

d = len(str(N))
start = max(0, N - 9 * d)

for i in range(start, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)