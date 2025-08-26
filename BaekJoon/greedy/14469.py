import sys

input = sys.stdin.readline

N = int(input().strip())
cows = [tuple(map(int, input().split())) for _ in range(N)]


cows.sort(key=lambda x: x[0])

t = 0
for a, b in cows:
    if t < a:
        t = a       
    t += b        
      
print(t)