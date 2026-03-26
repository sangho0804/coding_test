# 색종이 만들기
# NxN paper ( n = 2^k)

import sys
input = sys.stdin.readline

w_cnt = 0
b_cnt = 0


def search_num_of_paper(paper, n):
    global w_cnt, b_cnt

    total = sum(sum(row) for row in paper)

    if total == n * n:
        b_cnt += 1
        return
    elif total == 0 :
        w_cnt += 1
        return 
    
    half = n // 2
    top_left     = [row[:half] for row in paper[:half]]
    top_right    = [row[half:] for row in paper[:half]]
    bottom_left  = [row[:half] for row in paper[half:]]
    bottom_right = [row[half:] for row in paper[half:]]

    for part in [top_left, top_right, bottom_left, bottom_right]:
        search_num_of_paper(part, half)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

search_num_of_paper(paper, N)
print(w_cnt)
print(b_cnt)


