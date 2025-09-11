# my code 
import sys
rd = sys.stdin.readline
w = sys.stdout.write

T = int(rd())


for _ in range(T):

    stack = []
    ins = rd().strip()
    
    if ins[0] == ')':
            print('NO')
            
    elif ins[-1] == '(':
            print('NO')
                   
    else:
        try:
            for i in range(0, len(ins)):
                if ins[i] == '(':
                    stack.append(ins[i])
                    # print(stack)
                else:
                    stack.pop()

        except IndexError:
             # print(stack)
             print('NO')
             continue
        
        if len(stack) != 0 :
             print('NO')

        else:
            #  print(stack)
             print('YES')
                

                    
                        
# gpt code 
# import sys
# rd = sys.stdin.readline
# w = sys.stdout.write

# T = int(rd())
# ans = []

# for _ in range(T):
#     s = rd().strip()
#     bal = 0
#     ok = True

#     for ch in s:
#         if ch == '(':
#             bal += 1
#         else:            # ch == ')'
#             bal -= 1
#             if bal < 0:  # 닫는 괄호가 더 많아지면 즉시 실패
#                 ok = False
#                 break

#     ans.append("YES" if ok and bal == 0 else "NO")

# w("\n".join(ans))