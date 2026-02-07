import sys
input = sys.stdin.readline

k = int(input())
idx, p = 0, 1

while p < k :
    p = pow(2, idx)
    idx += 1

def solve(k, p, ans) :
    if p == 1 :
        return ans
    mid = p//2
    if ans == 0 :
        if k<=mid :
            return solve(k, mid, 0)
        else :
            return solve(k-mid, mid, 1)
    else :
        if k<=mid :
            return solve(k, mid, 1)
        else :
            return solve(k-mid, mid, 0)   

print(solve(k, p, 0))