# 2005 파스칼 삼각형

import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input().strip())

    start = 1
    arr = [0,1]

    for i in range(1,1+N):
        for j in range(0, i):
            arr[i-j] = arr[i-j] + arr[i-j-1]
        
            print(arr[i-j], end=' ')
        arr.append(0)
        print()
