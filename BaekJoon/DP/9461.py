import sys
rd = sys.stdin.readline
w = sys.stdout.write

T = int(rd().strip())

ans = []
for _ in range(T):
    _case = int(rd().strip())
    arr = [1, 1, 1, 2, 2]

    if _case <= 5 :
        ans.append(arr[_case-1])
    
    else:
        for i in range(6, _case+1):

            t = arr[i-2] + arr[i-6]
            arr.append(t)
        ans.append(arr[_case-1])


w('\n'.join(str(x) for x in (ans)))
