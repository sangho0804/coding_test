import sys

rd = sys.stdin.readline

A = int(rd())
B = int(rd())
C = int(rd())

result = A * B * C
s = str(result)

for i in range(10):
    print(s.count(str(i)))