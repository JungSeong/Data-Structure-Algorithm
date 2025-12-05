def solution(board, moves):
    answer = 0
    moves = list(map(lambda x : x-1, moves))
    board = list(map(list, zip(*board)))
    basket = []
    
    for row in board :
        row.reverse()
    
    for col in moves :
        for i in range(len(board[0])-1, -1, -1) :
            if board[col][i] != 0 :
                popped_doll = board[col][i]
                board[col][i] = 0
                basket.append(popped_doll)
                break
        if len(basket) >= 2 and basket[-1] == basket[-2] :
            basket.pop()
            basket.pop()
            answer += 2

    return answer