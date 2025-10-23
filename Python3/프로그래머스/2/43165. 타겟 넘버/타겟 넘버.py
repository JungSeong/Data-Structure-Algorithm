# DFS

def DFS(numbers, cur, idx, target):    
    if idx == len(numbers) :
        if cur == target :
            return 1
        else :
            return 0
    
    total_count = 0
    
    operation = [-1, 1]
    for op in operation :
        total_count += DFS(numbers, cur + op * numbers[idx], idx+1, target)
        
    return total_count

def solution(numbers, target):
    answer = 0
    answer = DFS(numbers, 0, 0, target)
    
    return answer