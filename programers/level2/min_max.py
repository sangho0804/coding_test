def solution(s):
    test = list(map(int, s.split()))
    
    return str(min(test)) + " " + str(max(test))
