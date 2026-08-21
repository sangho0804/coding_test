# 2819. 격자판의 숫자 이어 붙이기 (DFS)
import sys

input = sys.stdin.readline

T = int(input())

def search_str(word, board, x, y, ans):
    
    if len(word) == 7 :
        ans.add(word)
        return
    
    iy = [-1, 1, 0, 0]
    ix = [0, 0, 1, -1]

    for i in range(4):
        c_y = iy[i] + y
        c_x = ix[i] + x
        if 0 <= c_y < 4 and 0 <= c_x < 4 :
            search_str(word + board[c_y][c_x], board, c_x, c_y, ans)

 
for tc in range(1, T+1):
    board = [list(map(str, input().split())) for _ in range(4)]
       
    ans = set()

    # print(board)

    for y in range(4):
        for x in range(4):
            word = board[y][x]
            search_str(word, board, x, y, ans)

    print(f"#{tc} {len(ans)}")