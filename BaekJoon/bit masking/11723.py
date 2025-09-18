# # my code 5328 ms
# import sys
# rd = sys.stdin.readline

# M = int(rd())

# arr = [[x, 0] for x in range(1, 21, 1)]


# for _ in range(M):
#     comd = list(rd().split())

#     legth = len(comd)

#     if legth > 1 :
#         idx = int(comd[1])

#         if comd[0] == 'add':    
#             if arr[idx-1][1] > 0 :
#                 continue
#             else:
#                 arr[idx-1][1] += 1

#         elif comd[0] == 'remove':
#             if arr[idx-1][1] == 0 :
#                 continue
#             else:
#                 arr[idx-1][1] -= 1

#         elif comd[0] == 'check':
#             if arr[idx-1][1] > 0 :
#                 print(1)
#             else:
#                 print(0)

#         elif comd[0] == 'toggle' :
#             if arr[idx-1][1] > 0 :
#                 arr[idx-1][1] -= 1
#             else:
#                 arr[idx-1][1] += 1
#     else:
#         if comd[0] == 'all':
#             for i in range(20):
#                 arr[i][1] = 1

#         else:
#             for i in range(20):
#                 arr[i][1] = 0
        

# gpt code 3088 ms
import sys
input = sys.stdin.readline

M = int(input())
S = 0                       # 공집합

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'add':
        x = int(cmd[1])
        S |= (1 << (x - 1))

    elif cmd[0] == 'remove':
        x = int(cmd[1])
        S &= ~(1 << (x - 1))

    elif cmd[0] == 'check':
        x = int(cmd[1])
        x = '1' if (S & (1 << (x - 1))) else '0'
        print(x)

    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        S ^= (1 << (x - 1))

    elif cmd[0] == 'all':
        S = (1 << 20) - 1  

    elif cmd[0] == 'empty':
        S = 0
