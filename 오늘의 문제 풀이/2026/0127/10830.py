import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
A_T = list(map(list, zip(*A)))
I = []

for i in range(N) :
    l = [0]*N
    l[i] = 1
    I.append(l)     

def pm(A, A_T) :
    result = []
    for row in A :
        l = []
        for col in A_T :
            l.append(sum(map(lambda x, y : x*y, row, col))%1000)
        result.append(l)
    return result

def transpose(A) :
    return list(map(list, zip(*A)))

def solve(B) :
    if B == 0 :
        return I
    elif B % 2 == 0 :
        half = solve(B//2)
        return pm(half, transpose(half)) 
    else :
        half = solve((B-1)//2)
        return pm(pm(half, transpose(half)), transpose(A))

for row in solve(B) :
    print(*row)