import sys
from itertools import combinations
INPUT = sys.stdin.readline
cnt, i = 0, 1
l = list(range(10))
full_combinations = []
decreasing_combinations = []
N = int(INPUT())

while True :
    if i > 10 :
        print(-1)
        exit()
    comb = list(combinations(l,i))
    full_combinations.extend(comb)
    print(full_combinations)
    cnt = len(full_combinations)
    if cnt >= N :
        break
    i += 1

for row in full_combinations :
    sorted_row = sorted(row, reverse=True)
    decreasing_number_str = "".join(map(str, sorted_row))
    decreasing_combinations.append(int(decreasing_number_str))

decreasing_combinations.sort()
print(decreasing_combinations[N-1])