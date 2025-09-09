# import sys
# rd = sys.stdin.readline

# N, M = map(int, rd().split())
# board = [rd().strip() for _ in range(N)]

# INF = 10**9
# ans = INF

# for y in range(N - 7):          
#     for x in range(M - 7):      
#         repaint_if_W = 0        
#         for i in range(8):
#             for j in range(8):
#                 expected = 'W' if (i + j) % 2 == 0 else 'B'
#                 if board[y + i][x + j] != expected:
#                     repaint_if_W += 1

#         repaint_if_B = 64 - repaint_if_W

#         ans = min(ans, repaint_if_W, repaint_if_B)

# print(ans)

# gpt hard cording // bit mask 
import sys
rd = sys.stdin.readline

def popcount(x: int) -> int:
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt

N, M = map(int, rd().split())

rows = []
for _ in range(N):
    s = rd().strip()
    bits = 0
    for j, ch in enumerate(s):
        if ch == 'W':
            bits |= (1 << j)
    rows.append(bits)

MASK_EVEN = 0b10101010  # 170
MASK_ODD  = 0b01010101  # 85
wmasks = [MASK_EVEN if (i & 1) == 0 else MASK_ODD for i in range(8)]

ans = 64
Nm7 = N - 7
Mm7 = M - 7

for y in range(Nm7):
    r0 = rows[y]     ; r1 = rows[y+1]
    r2 = rows[y+2]   ; r3 = rows[y+3]
    r4 = rows[y+4]   ; r5 = rows[y+5]
    r6 = rows[y+6]   ; r7 = rows[y+7]
    for x in range(Mm7):
        c  = popcount(((r0 >> x) & 255) ^ wmasks[0])
        c += popcount(((r1 >> x) & 255) ^ wmasks[1])
        c += popcount(((r2 >> x) & 255) ^ wmasks[2])
        c += popcount(((r3 >> x) & 255) ^ wmasks[3])
        c += popcount(((r4 >> x) & 255) ^ wmasks[4])
        c += popcount(((r5 >> x) & 255) ^ wmasks[5])
        c += popcount(((r6 >> x) & 255) ^ wmasks[6])
        c += popcount(((r7 >> x) & 255) ^ wmasks[7])

        repaint = c if c <= 32 else 64 - c
        if repaint < ans:
            ans = repaint

print(ans)
