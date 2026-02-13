import sys
input = sys.stdin.readline

board = input().rstrip() + "_"
cnt = 0
answer = []

for i in range(len(board)) :
    if board[i] == "X" :
        cnt += 1
        if cnt == 4 :
            answer.append("AAAA")
            cnt = 0
    elif board[i] == "." :
        if cnt == 4 :
            answer.append("AAAA")
            cnt = 0
        elif cnt == 2 :
            answer.append("BB")
            cnt = 0
        elif cnt % 2 == 1 :
            print(-1)
            sys.exit(0)
        answer.append(".")
    else :
        if cnt == 4 :
            answer.append("AAAA")
        elif cnt == 2 :
            answer.append("BB")
        elif cnt % 2 == 1 :
            print(-1)
            sys.exit(0)

print(''.join(answer))