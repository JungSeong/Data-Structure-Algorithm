import sys
INPUT = sys.stdin.readline

N = int(INPUT())
taste = [tuple(map(int, INPUT().split())) for _ in range(N)]
answer = float('INF')

for i in range(1, (1 << N)) :
    sour = 1
    bitter = 0

    for j in range(N) :
        if i & (1 << j) :
            sour *= taste[j][0]
            bitter += taste[j][1]

    answer = min(answer, abs(sour-bitter))

print(answer)