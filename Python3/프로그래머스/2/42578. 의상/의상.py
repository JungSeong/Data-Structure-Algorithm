from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(list)
    
    for cloth in clothes :
        d[cloth[1]].append(cloth[0])
        
    for v in d.values() :
        answer *= (len(v)+1)
        
    answer -= 1
    
    return answer