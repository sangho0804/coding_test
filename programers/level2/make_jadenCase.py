def solution(s):
    s = str.title(s)
    s = list(s)
    for i in range(len(s)):

        if s[i].isdigit():
            
            s[i+1] = s[i+1].lower()
    
    s = ''.join(s)

        
    return s