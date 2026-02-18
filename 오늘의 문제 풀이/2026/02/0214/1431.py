import sys
input = sys.stdin.readline

N = int(input())
serials = [input().rstrip() for _ in range(N)]
serials.sort(key=lambda x : (len(x), sum(int(c) for c in x if c.isdigit()), x))

for row in serials :
    print(row)