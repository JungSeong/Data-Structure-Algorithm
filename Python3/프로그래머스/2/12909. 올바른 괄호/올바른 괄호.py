from collections import deque

def solution(s):
    answer = True
    q = deque()
    
    for ch in s :
        if ch == '(' : q.append('(')
        else :
            if len(q) != 0 :
                q.pop()
            else :
                answer = False
                return answer
        
    if len(q) == 0 : answer = True
    else : answer = False

    return answer