# 11724 연결 요소의 개수

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        queue = deque([i])

        visited[i] = True
        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

print(count)