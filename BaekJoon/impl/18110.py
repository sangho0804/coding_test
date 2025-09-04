import sys
rd = sys.stdin.readline

n = int(rd().strip())

if n == 0:
    print(0)
    sys.exit(0)

arr = [int(rd()) for _ in range(n)]
arr.sort()

k = (n * 15 + 50) // 100 

total = sum(arr[k:n - k])
cnt = n - 2 * k

ans = int(total / cnt + 0.5)
print(ans)
