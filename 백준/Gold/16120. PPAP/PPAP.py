import sys
input = sys.stdin.readline

st = input().rstrip()
answer = []
ppap = "PPAP"

for i in range(len(st)) :
    answer.append(st[i])
    if len(answer) >= len(ppap) and ''.join(answer[-len(ppap):]) == ppap :
        for i in range(len(ppap)) :
            answer.pop()
        answer.append("P")

if ''.join(answer) == "P" :
    print("PPAP")
else :
    print("NP")