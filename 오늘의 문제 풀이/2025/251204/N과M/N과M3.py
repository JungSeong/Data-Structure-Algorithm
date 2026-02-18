import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
results: list[str] = []
current_path : list[int] = []

def BackTracking(k: int) -> None :
    if k == M :
        results.append(" ".join(map(str, current_path)))
        return
    for i in range(1, N+1) :
        current_path.append(i)
        BackTracking(k+1)
        current_path.pop()

BackTracking(0)

for row in results :
    print(row)