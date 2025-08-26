# 백준 1260 : DFS와 BFS

import sys
sys.setrecursionlimit(10**6)
from collections import deque

# N 정정 개수, link 간선 개수, V 정점
N, link, V = map(int, input().split())

# Adjacency List init
graph = [[] for _ in range(N+1)]

for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# sorting Adjacency List
for g in graph:
    g.sort()
    
# make dfs
def dfs(graph, v, visited, order):
    if visited[v]:
        return
    visited[v] = True
        
    order.append(v)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, order)
            

# 2. BFS 만들기

def bfs(graph, start, visited, order):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        order.append(v)
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)


# visit check, logic flag
visited_1 = [False]*(N+1) # dfs
visited_2 = [False]*(N+1) # bfs
order_dfs, order_bfs = [], []
            
dfs(graph, V, visited_1, order_dfs)
bfs(graph, V, visited_2, order_bfs)

print(*order_dfs)
print(*order_bfs)
