import sys
input = sys.stdin.readline

st = input().rstrip()
alphabets = [[0]*(len(st)+1) for _ in range(26)]

for i in range(len(st)) :
    idx = ord(st[i])-ord('a')
    for j in range(26) :
        alphabets[j][i+1] = alphabets[j][i]
    alphabets[idx][i+1] += 1

q = int(input())
ans = []

for i in range(q) :
    ai, li, ri = input().split()
    idx, li, ri = ord(ai)-ord('a'), int(li), int(ri)
    ans.append(str(alphabets[idx][ri+1]-alphabets[idx][li]))

print("\n".join(ans))