import sys
input = sys.stdin.readline

N = int(input())
chickens = list(map(int, input().split()))
k = int(input())

target_size = N // k

def solve(start, end) :
    if end - start == target_size :
        return sorted(chickens[start:end])
    else :
        mid = (start+end)//2
        left, right = solve(start, mid), solve(mid, end)
        return left + right

print(*solve(0, N))