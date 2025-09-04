# my code 112 ms
import sys
from collections import deque
rd = sys.stdin.readline
w = sys.stdout.write

N, K = map(int, rd().split())
que = deque(i+1 for i in range(N))
arr = []
count = 1

while que:
    if count < K:                
        que.append(que.popleft())
        count += 1
    else:                        
        arr.append(que.popleft())
        count = 1                 

print("<" + ", ".join(map(str, arr)) + ">")


# gpt code 56ms
# import sys
# from collections import deque

# def main():
#     input = sys.stdin.readline
#     N, K = map(int, input().split())

#     q = deque(range(1, N + 1))
#     ans = []

#     while q:
#         q.rotate(-(K - 1))   # K번째가 맨 앞으로 오도록 왼쪽 회전
#         ans.append(q.popleft())

#     # 형식: <3, 6, 2, 7, 5, 1, 4>
#     print("<" + ", ".join(map(str, ans)) + ">")

# if __name__ == "__main__":
#     main()

