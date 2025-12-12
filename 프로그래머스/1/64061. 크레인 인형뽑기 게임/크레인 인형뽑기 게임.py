def solution(board, moves):
    answer = 0
    board_T = list(map(list, zip(*board)))
    s = []
    moves = map(lambda x : x-1, moves)
    N, M = len(board), len(board[0])
    cnt = 0
    
    for row in moves :
        for i in range(M) :
            if board_T[row][i] != 0 :
                popped = board_T[row][i]
                board_T[row][i] = 0
                s.append(popped)
                break
        
        if len(s) >= 2 :
            if s[-1] == s[-2] :
                s.pop()
                s.pop()
                cnt += 2
                
    answer = cnt
    
    return answer