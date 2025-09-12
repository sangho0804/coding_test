import sys
sys.setrecursionlimit(10**6)
rd = sys.stdin.readline

N, M = map(int, rd().split())
board = [list(map(int, rd().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, depth, total):
    global ans
    if depth == 4:
        ans = max(ans, total)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total + board[nx][ny])
            visited[nx][ny] = False

def check_T(x, y):
    global ans
    # 중심 + 주변 4칸 중 3칸을 선택
    center = board[x][y]
    temp = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            temp.append(board[nx][ny])
    if len(temp) >= 3:
        temp.sort(reverse=True)
        ans = max(ans, center + temp[0] + temp[1] + temp[2])

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_T(i, j)

print(ans)