import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []
S = [0] * (N+1)
start = 0

for i in range(1, N+1) :
    S[i] = S[i-1] + A[i-1]

for i in range(Q) :
    queries.append(list(map(int, input().split())))

for query in queries :
    if query[0] == 1 :
        start = (start + N - query[1]) % N
    elif query[0] == 2 :
        start = (start + query[1]) % N
    else :
        a, b = query[1]-1, query[2]
        a = (a + start) % N
        b = (b + start) % N
        if a > b :
            print(sum(A[a:N]) + sum(A[:b]))
        else :
            print()