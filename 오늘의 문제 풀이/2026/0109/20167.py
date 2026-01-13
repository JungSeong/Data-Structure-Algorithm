# 누적된 만족도가 K 이상 or 더 이상 먹을 먹이가 없을 때 멈춤
# 최소 만족도 이상이 되면 초과분만큼 탈피 에너지 저장 & 만족도는 다시 0이
# 되고 먹이를 먹을 수 있음

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
