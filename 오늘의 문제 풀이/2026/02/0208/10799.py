import sys
input = sys.stdin.readline

pipe = input().rstrip()
s = []
answer = 0
before = ""

for ch in pipe :
    before = ch
    if ch == '(' :
        s.append('(')
    else :
        s.pop()
        if before == '(' :
            answer += len(s)
    print(before)

print(answer)