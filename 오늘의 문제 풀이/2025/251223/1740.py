import sys
INPUT = sys.stdin.readline

N = int(INPUT())
N = format(N, 'b')
answer = int(N, 3)
print(answer)