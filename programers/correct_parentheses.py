from collections import deque

def solution(s):
    answer = True
    que = deque()
    s = list(s)
    
    for i in s :
        if i == '(' :
            que.append(i)
        else:
            if len(que) == 0 :
                answer = False
                break
            else: 
                que.pop()
                
    if len(que) != 0 :
        answer = False

    

    return answer