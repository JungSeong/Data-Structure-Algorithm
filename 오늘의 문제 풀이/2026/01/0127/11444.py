import sys
input = sys.stdin.readline

n = int(input())
I = [[1,0],[0,1]]
A = [[1,1],[1,0]]

def pow_matrix(A, A_T) :
    answer = []
    for row in A :
        l = []
        for col in A_T :
            l.append(sum(map(lambda x, y : x*y, row, col)) % 1000000007)
        answer.append(l)
    return answer

def transpose(A) :
    return list(map(list, zip(*A)))

def solve(n) :
    if n == 0 :
        return I
    elif n%2 == 1 :
        half = solve((n-1)//2)
        return pow_matrix(pow_matrix(half, transpose(half)), transpose(A))
    else :
        half = solve(n//2)
        return pow_matrix(half, transpose(half))

final = solve(n)
print(final[0][1])