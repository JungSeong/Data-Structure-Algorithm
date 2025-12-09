from collections import deque

def solution(board):
    MAX_COST = 10**9
    answer = MAX_COST
    move = [(-1,0),(0,1),(1,0),(0,-1)]
    N = len(board[0])
    
    m = [[[MAX_COST] * N for _ in range(N)] for _ in range(4)]
    dq = deque()
    dq.append([2,0,0]) # 아래로 이동
    dq.append([1,0,0]) # 오른쪽으로 이동
    m[2][0][0] = 0
    m[1][0][0] = 0

    while dq :
        pos, cur_r, cur_c = dq.popleft()
        cost = 0
        if cur_r == N-1 and cur_c == N-1 :
            answer = min(m[pos][cur_r][cur_c], answer)
            continue
        for i in range(4) :
            dr, dc = move[i]
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<=N-1 and 0<=new_c<=N-1 and board[new_r][new_c] == 0 :
                if pos == i : cost = 100
                else : cost = 600
                if m[i][new_r][new_c] > m[pos][cur_r][cur_c] + cost :
                    m[i][new_r][new_c] = m[pos][cur_r][cur_c] + cost
                    dq.append([i, new_r, new_c])
    
    return answer