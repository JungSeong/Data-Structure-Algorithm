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