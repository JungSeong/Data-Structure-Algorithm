import sys
input = sys.stdin.readline

S = input().rstrip()
inTag = False
answer = []

final = ""
s = []

for i in range(len(S)) :
    if S[i] == "<" :
        final += ''.join(reversed(s))
        inTag = True
        final += "<"
        s = []
    elif S[i] == ">" :
        inTag = False
        final += ''.join(s)
        final += ">"
        s = []
    elif S[i] == " " :
        if inTag :
            s.append(" ")
        else :
            final += ''.join(reversed(s))
            final += " "
            s = []
    else :
        s.append(S[i])

final += ''.join(reversed(s))
answer.append(final)

print(' '.join(answer))