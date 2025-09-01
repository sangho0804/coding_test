import sys
from collections import deque

rd = sys.stdin.buffer.readline

t = int(rd())
out_lines = []

for _ in range(t):
    n, m = map(int, rd().split())
    arr = list(map(int, rd().split()))

    q = deque((p, i) for i, p in enumerate(arr))  
    cnt = [0]*10
    for p in arr:
        cnt[p] += 1

    cur = 9
    while cur > 0 and cnt[cur] == 0:
        cur -= 1

    printed = 0
    while True:
        p, i = q[0]
        if p == cur:                 # 지금 뽑을 차례
            q.popleft()
            printed += 1
            cnt[p] -= 1
            if i == m:               # 내가 찾는 문서면 종료
                out_lines.append(str(printed))
                break
            # 다음 최대 중요도 갱신
            while cur > 0 and cnt[cur] == 0:
                cur -= 1
        else:
            q.rotate(-1)             # 뒤로 보내기

sys.stdout.write("\n".join(out_lines))