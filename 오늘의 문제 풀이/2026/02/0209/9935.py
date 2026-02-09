import sys
input = sys.stdin.readline

st = input().rstrip()
bomb = input().rstrip()
answer = []

for ch in st :
    answer.append(ch)
    if len(answer) >= len(bomb) and "".join(answer[-len(bomb):]) == bomb :
        for i in range(len(bomb)) :
            answer.pop()

if len(answer) > 0 :
    print(''.join(answer))
else :
    print("FRULA")