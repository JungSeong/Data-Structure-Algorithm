import sys
input = sys.stdin.readline

board = list(list(input().rstrip()) for _ in range(8))
result = 0

for i in range(8) :
    for j in range(8) :
        if i%2==0 and j%2==0 and board[i][j]=='F' :
            result += 1
        elif i%2==1 and j%2==1 and board[i][j]=='F' :
            result += 1

print(result)