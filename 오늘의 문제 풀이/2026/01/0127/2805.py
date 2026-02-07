import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

min_len, max_len = 0, trees[-1]

def get_max_height(min_len, max_len) :
    if min_len >= max_len : return max_len
    elif min_len == max_len-1 : return min_len
    mid = (min_len+max_len)//2
    cnt = 0
    for height in trees :
        if height-mid > 0 :
            cnt += height-mid
    if cnt >= M :
        answer = get_max_height(mid, max_len)
    else :
        answer = get_max_height(min_len, mid)
    
    return answer

answer = get_max_height(min_len, max_len)
print(answer)