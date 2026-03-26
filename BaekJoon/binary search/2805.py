# claude.ai 

import sys
input = sys.stdin.readline
 
def solve():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    lo, hi = 0, max(trees)
    
    while lo < hi:
        mid = (lo + hi + 1) // 2
        # mid 높이로 잘랐을 때 얻는 나무 총량
        total = sum(t - mid for t in trees if t > mid)
        
        if total >= M:
            lo = mid  # 더 높일 수 있음
        else:
            hi = mid - 1  # 높이를 낮춰야 함
    
    print(lo)
 
solve()
               