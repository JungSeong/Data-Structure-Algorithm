from collections import defaultdict
import decimal

def solution(N, stages):
    answer = []
    failed_person = [0] * (N+1)
    total_person = [0] * (N+1)
    
    for col in stages :
        for i in range(1, col) :
            total_person[i] += 1
        if col != N+1 :
            failed_person[col] += 1
            total_person[col] += 1
    
    failed_rate = defaultdict()
    for i in range(1, N+1) :
        if total_person[i] == 0 :
            failed_rate[i] = 0.0
        else :
            failed_rate[i] = decimal.Decimal(failed_person[i]) / decimal.Decimal(total_person[i]) # 이것도 잘 몰랐음
        
    val = sorted(failed_rate.items(), key=lambda x : (-x[1], x[0])) # 이거 잘 몰랐음
    for col in val :
        answer.append(col[0])
    
    return answer