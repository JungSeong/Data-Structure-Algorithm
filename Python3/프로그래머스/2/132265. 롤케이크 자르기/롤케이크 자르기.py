# nlog(n)
# 전체 배열 길이 // 2 까지 해서
# 0~idx & 나머지 -> set() 크기 비교해서 같으면 

from collections import defaultdict, Counter

def solution(topping):
    answer = 0
    a = defaultdict(int)
    b = Counter(topping)
    len_a, len_b = len(a), len(b)
    
    for i in range(len(topping)) :
        if a[topping[i]] == 0 : len_a += 1
        a[topping[i]] += 1
        b[topping[i]] -= 1
        if b[topping[i]] == 0 : len_b -= 1
        
        if len_a == len_b : answer += 1
     
    return answer