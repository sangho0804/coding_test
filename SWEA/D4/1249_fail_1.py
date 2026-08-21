#1249. [S/W 문제해결 응용] 4일차 - 보급로
import sys
import heapq
import math
INF = 1e8

input = sys.stdin.readline

def dijkstra(graph, start): 
    distances = [float('inf') for _ in range(N*N)]
    distances[start]= 0
    pq = [(0, start)] 
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    _map = [list(map(int, input().rstrip())) for _ in range(N)]
    graph = [[] for _ in range(N*N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            for v in range(4):
                if i + dy[v] > -1 and j + dx[v] > -1 and i + dy[v] < N and j + dx[v] < N :
                    _y = i + dy[v]
                    _x = j + dx[v]
                    graph[i*N + j].append((_y*N + _x, _map[_y][_x]))
    #print(graph)

    dist = dijkstra(graph, 0)
    

    
    print(f"#{tc} {dist[len(dist) - 1]}")

assert False
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(board, N):
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]  # 비용, y, x

    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    while pq:
        cost, y, x = heapq.heappop(pq)

        if cost > dist[y][x]:
            continue

        if y == N - 1 and x == N - 1:
            return cost

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N and 0 <= nx < N:
                new_cost = cost + board[ny][nx]

                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost, ny, nx))

    return dist[N - 1][N - 1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]

    answer = dijkstra(board, N)

    print(f"#{tc} {answer}")