# 2930. 힙 
import sys
import heapq

input = sys.stdin.readline


T = int(input())

for tc in range(1, T+1):
    que = []
    N = int(input().strip())
    ans = f"#{tc}"
    for n in range(N):
        arr = list(map(int, input().split()))

        if arr[0] == 1:
            heapq.heappush(que, (-arr[1], arr[1]))
        else : 
            if len(que) < 1:
                ans += " -1"
            else:
                maxValue = heapq.heappop(que)[1]
                ans = ans + " " + str(maxValue)

    print(ans)