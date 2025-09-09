import sys
rd = sys.stdin.readline

n = int(rd())
arr = []
for _ in range(n):
    comd = list(rd().split())

    if comd[0] == 'push':
        
        arr.append(comd[1])

    if comd[0] == 'pop':
        p = -1 if  len(arr) == 0 else arr.pop(0)
        print(p)
        
    if comd[0] == 'size':
        print(len(arr))

    if comd[0] == 'empty':
        bol = 1 if len(arr) == 0 else 0
        print(bol)

    if comd[0] == 'front':
        f = -1 if len(arr) == 0 else arr[0]
        print(f)

    if comd[0] == 'back':
        b = -1 if len(arr) == 0 else arr[-1]
        print(b)
    