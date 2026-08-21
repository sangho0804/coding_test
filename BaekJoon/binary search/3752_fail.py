#3752. 가능한 시험 점수

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    max_score = sum(scores)

    # dp[i] = i점을 만들 수 있는가?
    dp = [False] * (max_score + 1)
    dp[0] = True

    for score in scores:
        # 뒤에서부터 탐색해야 현재 score를 중복해서 사용하지 않음
        for i in range(max_score - score, -1, -1):
            if dp[i]:
                dp[i + score] = True

    answer = sum(dp)

    print(f"#{tc} {answer}")
