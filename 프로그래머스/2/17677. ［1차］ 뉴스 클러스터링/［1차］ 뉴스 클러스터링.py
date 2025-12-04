from collections import defaultdict

def solution(str1, str2):
    answer = 0
    set1 = defaultdict(int)
    set2 = defaultdict(int)
    keys = set()

    for i in range(len(str1)-1) :
        ch = str1[i]+str1[i+1]
        CH = ch.upper()
        if 'A'<=CH[0]<='Z' and 'A'<=CH[1]<='Z' :
            set1[CH] += 1
            keys.add(CH)
    
    for i in range(len(str2)-1) :
        ch = str2[i]+str2[i+1]
        CH = ch.upper()
        if 'A'<=CH[0]<='Z' and 'A'<=CH[1]<='Z' :
            set2[CH] += 1
            keys.add(CH)
    
    gyo, hap = 0, 0
    for k in keys :
        gyo += min(set1[k], set2[k])
        hap += max(set1[k], set2[k])
    
    # 둘 다 공집합
    if gyo == 0 and hap == 0 :
        answer = 65536
    else :
        answer = int(gyo/hap*65536)
    
    return answer