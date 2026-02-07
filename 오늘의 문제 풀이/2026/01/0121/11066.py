# 하나의 파일로 합칠 때 필요한 최소 비용

import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for t in range(T) :
    K = int(input())
    dp = [[0]*K for _ in range(K)]
    files = list(map(int, input().split()))
    S = [0]*(K+1)
    for i in range(len(files)) :
        S[i+1] = files[i]+S[i]
    print(S)