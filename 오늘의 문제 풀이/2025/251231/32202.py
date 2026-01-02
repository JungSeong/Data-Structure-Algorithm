# 모든 학생이 현이 or 짝꿍에게 풀이 들음
# 연속된 두 줄 중 적어도 한 줄은 짝꿍에게의 풀이 전달이 이루어 짐
# 학생을 부를 수 있는 모든 경우의 수?

import sys
input = sys.stdin.readline
mod = 10**9+7

N = int(input())
a = 2
b = 1

for i in range(1, N) :
    new_a = 2 * (a+b) % mod
    new_b = a % mod

    a, b = new_a, new_b

print((a+b) % mod)