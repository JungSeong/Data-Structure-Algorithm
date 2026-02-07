import sys
input = sys.stdin.readline

def solve(p) :
    if p == 1 :
        return "-"
    prev = solve(p//3)
    return prev + " "*(p//3) + prev

while True :
    try :
        N = int(input())
        p = pow(3, N)
        print(solve(p))
    except :
        break