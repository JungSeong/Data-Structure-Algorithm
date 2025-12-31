import sys
input = sys.stdin.readline

a = 2
b = 1

N = int(input())

for i in range(1, N) :
    new_a = a*1 + b*2
    new_b = a+b
    a, b = new_a % 9901, new_b % 9901

print((a+b) % 9901)