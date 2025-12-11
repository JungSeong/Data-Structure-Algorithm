from collections import Counter

def str_to_counter(str) :
    s = []
    for i in range(len(str)-1) :
        ch = str[i:i+2]
        ch = ch.upper()
        if ch.isalpha() :
            s.append(ch)
            
    c = Counter(s)  
    return c 

def solution(str1, str2):
    answer = 0
    counter1 = str_to_counter(str1)
    counter2 = str_to_counter(str2)
    
    union_set = list((counter1|counter2).elements())
    intersect_set = list((counter1&counter2).elements())
    
    if len(intersect_set) == 0 and len(union_set) == 0 :
        answer = 65536    
    else :
        answer = int(len(intersect_set)/len(union_set)*65536)
    
    return answer