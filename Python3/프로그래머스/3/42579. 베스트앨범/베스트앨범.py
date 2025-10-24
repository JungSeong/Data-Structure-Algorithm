# 장르 | plays + idx dict
# 먼저 들어갈 장르 결정
# 많이 재생된 노래 TOP 2 answer에 넣는 로직

from collections import defaultdict

def solution(genres, plays):
    answer = []
    d = defaultdict(list)
    cnt = defaultdict(int)
    
    for i, genre in enumerate(genres) :
        d[genre].append([plays[i], i])
        cnt[genre] += plays[i]
        
    # 먼저 들어갈 장르 결정
    sorted_cnt = sorted(cnt.items(), key = lambda x : x[1], reverse=True)
    
    for cnt in sorted_cnt :
        genre = cnt[0]
        # 장르에 속한 곡이 하나인 경우
        if len(d[genre]) == 1 : answer.append(d[genre][0][1])
        else : # 하나 이상인 경우
            selected = d[genre]
            sorted_selected = sorted(selected, key = lambda x : (-x[0], x[1]))
            top_2 = sorted_selected[:2]
            
            for t in top_2 :
                answer.append(t[1])
    
    return answer