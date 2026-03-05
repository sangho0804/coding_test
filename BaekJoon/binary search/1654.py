import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = []
for i in range(K):
    arr.append(int(input()))

left, right = 1, max(arr)

result = 0
while left <= right:
    mid = (left + right) // 2
    count = sum(x // mid for x in arr)

    if count >= N:
        result = mid      # 조건 만족 → 더 길게 시도
        left = mid + 1
    else:
        right = mid - 1   # 너무 길어서 개수 부족 → 더 짧게

print(result)