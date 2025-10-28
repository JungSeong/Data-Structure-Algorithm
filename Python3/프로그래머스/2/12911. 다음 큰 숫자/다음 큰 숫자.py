def solution(n):
    answer = 0
    bn = format(n, 'b')
    cnt = bn.count("1")
    
    while True :
        n += 1
        bn = format(n, 'b')
        if cnt == bn.count("1") :
            answer = n
            break
    
    return answer