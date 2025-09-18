# my code 46856kb , 112 ms
import sys
from collections import Counter
rd = sys.stdin.readline
w = sys.stdout.write

N, M = map(int, rd().split())

arr = []

for i in range(N+M):
    name = rd().strip()
    arr.append(name)


ans = []
counter = Counter(arr)
for x, y in counter.items():

    if y > 1:
        ans.append(x)

ans.sort()

print(len(ans))
w('\n'.join(ans))

# gpt code 43168 kb, 76 ms 
import sys
rd = sys.stdin.readline
w = sys.stdout.write

N, M = map(int, rd().split())

# 듣도 못한 사람 집합
heard = {rd().strip() for _ in range(N)}

seen = {rd().strip() for _ in range(M)}

both = sorted(heard & seen)  # 교집합 후 사전순 정렬

w(str(len(both)) + "\n")
w("\n".join(both))