# 1210. [S/W 문제해결 기본] 2일차 - Ladder1 (구현) (bitmask prac)
import sys

input = sys.stdin.readline

T = 10
UP    = 0b100
RIGHT = 0b010
LEFT  = 0b001

for tc in range(T):
    number = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    sy = 99
    sx = board[99].index(2)

    while sy > 0 :
        right = board[sy][sx + 1] if sx < 99 else 0
        left = board[sy][sx - 1] if sx > 0 else 0

        S = (right << 1) | left
        if S & LEFT:
            board[sy][sx] = 0
            sx -= 1
        elif S & RIGHT:
            board[sy][sx] = 0
            sx += 1
        else:
            sy -= 1

    print(f"#{number} {sx}")
    

    