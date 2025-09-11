import sys
rd = sys.stdin.readline

K = int(rd())

arr = []
for _ in range(K):
    ins = int(rd())
    if ins == 0 :
        arr.pop()
    else:
        arr.append(ins)

print(sum(arr))