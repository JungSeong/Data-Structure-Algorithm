from math import ceil

def solution(n,a,b):
    answer = 1
    
    while ceil(a/2) != ceil(b/2) :
        a = ceil(a/2)
        b = ceil(b/2)
        answer += 1

    return answer