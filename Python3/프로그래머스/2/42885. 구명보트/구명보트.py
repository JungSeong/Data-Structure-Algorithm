# 무조건 사람들 구출 가능
# 무게 제한 까지는 태울 수 있음
# 구명보트 최대 2명
# O(nlogn) 알고리즘?

def solution(people, limit):
    answer = 0
    people = sorted(people, reverse = True)
    
    length = len(people)
    isrode = 0
    
    i, j = 0, length - 1
    
    while isrode < length :
        if people[i] + people[j] > limit :
            answer += 1
            i += 1
            isrode += 1
        else :
            answer += 1
            i += 1
            j -= 1
            isrode += 2
    
    return answer