import sys
input = sys.stdin.readline

N = int(input())
m = list(list(map(int, input().split())) for _ in range(N))

def CNN_222(N, cur_r, cur_c) :
    if N == 2 :
        possible = []
        for i in range(2) :
            for j in range(2) :
                possible.append(m[cur_r+i][cur_c+j])
        possible.sort(reverse=True)
        return possible[1]
    else :
        answer = []
        top_left = CNN_222(N//2, cur_r, cur_c)
        top_right = CNN_222(N//2, cur_r+N//2, cur_c)
        bottom_left = CNN_222(N//2, cur_r, cur_c+N//2)
        bottom_right = CNN_222(N//2, cur_r+N//2, cur_c+N//2)
        answer = [top_left, top_right, bottom_left, bottom_right]
        answer.sort(reverse=True)
        return answer[1]

print(CNN_222(N, 0, 0))