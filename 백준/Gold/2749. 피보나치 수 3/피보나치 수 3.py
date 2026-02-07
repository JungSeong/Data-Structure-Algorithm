import sys
input = sys.stdin.readline

p = 1000000
n = int(input())
I = [[1,0],[0,1]]
A = [[1,1],[1,0]]

def transpose(A) :
    A_T = list(map(list, zip(*A)))
    return A_T

def mul(A, A_T) :
    result = []
    for row in A :
        answer = []
        for col in A_T :
            answer.append(sum(map(lambda x,y : x*y, row, col))%p)
        result.append(answer)
    return result

def pow_matrix(A, n) :
    if n == 0 :
        return I
    elif n % 2 == 1 :
        half = pow_matrix(A, (n-1)//2)
        return mul(mul(half, transpose(half)), A)
    else :
        half = pow_matrix(A, n//2)
        return mul(half, transpose(half))

print(pow_matrix(A, n)[0][1])