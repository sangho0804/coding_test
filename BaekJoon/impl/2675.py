import sys

rd = sys.stdin.readline
w = sys.stdout.write

n = int(rd())
out = []

for _ in range(n):
    r, s = rd().split()
    r = int(r)
    out.append("".join(ch * r for ch in s))

w("\n".join(out))
    
