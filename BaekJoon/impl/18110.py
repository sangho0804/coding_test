import sys
rd = sys.stdin.readline

n = int(rd())

arr = []
if n == 0 :
    print(0)

else :
    for _ in range(n):
        comment = int(rd())
        arr.append(comment)
    
