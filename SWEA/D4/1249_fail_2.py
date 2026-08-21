import sys
import heapq

input = sys.stdin.readline
INF = 1e8

T = int(input())


def dijkstra(graph, N):
    distance = [[INF] * N for _ in range(N)]

    distance[0][0] = 0
    pq = [(0, 0, 0)] # w, r, c

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while pq :
        cur_dist, curr_r, curr_c = heapq.heappop(pq)

        if cur_dist > distance[curr_r][curr_c] :
            continue

        if curr_c == N-1 and curr_r == N-1 :
            return cur_dist

        for i in range(4):
            ny = dy[i] + curr_r 
            nx = dx[i] + curr_c 

            if 0 <= ny < N and 0 <= nx < N :
                new_dist = cur_dist + graph[ny][nx]


                if new_dist < distance[ny][nx] :
                    distance[ny][nx] = new_dist
                    heapq.heappush(pq, (new_dist, ny, nx))

    return distance[N-1][N-1]
                       


for tc in range(1, T + 1):
    N = int(input().strip())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    result = dijkstra(graph, N)

    print(f"#{tc} {result}")
    
