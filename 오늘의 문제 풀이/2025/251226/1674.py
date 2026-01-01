# 모든 음식 독립 & 시간 T까지 섭취한 모든 음식에 대한 효과 반경의 합 = 안전 거리
# 효과 반경 음수 -> 영향 X
# 안전 거리 1 이상 유지
# 시간 순으로 주어지지 않을 수 있음

import sys
input_data = sys.stdin.read().splitlines() # 파일의 끝까지 한 번에 입력 받음

consumptions = []
queries = []

for line in input_data :
    parts = line.split()
    if parts[0] == "Query" :
        queries.append(int(parts[1]))
    else :
        consumptions.append(tuple(parts))

consumptions.sort()
queries.sort()

for T in queries :
    answer = 0.0
    for ops, t, N in consumptions :
        t, N = int(t), float(N)
        if t <= T :
            dt = T-t
            radius = 0.0
            if ops == "Chocolate" :
                radius = 8*N-dt/12
            else :
                radius = 2*N-(dt**2)/79
            if radius > 0 :
                answer += radius
    answer = max(answer, 1.0)
    print(f"{T} {answer:.1f}")