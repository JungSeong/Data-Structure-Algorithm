import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
results : list[str] = []
current : list[int] = []

def BackTracking(k: int, cur: int) -> None :
    if k == M :
        results.append(' '.join(map(str, current)))
        return
    for i in range(cur, N+1) :
        current.append(i)
        BackTracking(k+1, i)
        current.pop()

BackTracking(0, 1)

for row in results :
    print(row)