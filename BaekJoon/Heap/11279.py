import sys
import heapq
input = sys.stdin.readline

max_heap = []

N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
            
    else:
        heapq.heappush(max_heap, -x)
