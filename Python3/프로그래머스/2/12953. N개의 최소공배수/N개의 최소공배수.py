from math import gcd
from collections import deque

def solution(arr):
    answer = 0
    q = deque(arr)
    
    while len(q) > 1 :
        a = q.popleft()
        b = q.popleft()
        gc = gcd(a, b)
        lcm = gc * (a // gc) * (b // gc)
        q.appendleft(lcm)
        
    answer = q[0]
    
    return answer