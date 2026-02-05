import sys
input = sys.stdin.readline

N = int(input())
S, k = 3, 0

while True :
    if N <= S :
        break
    else :
        k += 1
        S = 2*S+(k+3)

def FindCh(S, k, cur) :
    answer = "o"
    if k == 0 :
        if cur == 1 :
            answer = "m"
        return answer
    half=(S-(k+3))//2
    left, right = half, half+k+3 
    if 0<=cur<=left :
        return FindCh(half, k-1, cur)
    elif left+1<=cur<=right :
        cur = cur - half
        if cur == 1 :
            answer = "m"
        return answer
    else :
        return FindCh(half, k-1, cur-right)

print(FindCh(S, k, N))