import sys
input = sys.stdin.readline

S = input().rstrip()
inTag = False
answer = []

final = []
s = []

for i in range(len(S)) :
    if S[i] == "<" :
        final.append(''.join(reversed(s)))
        inTag = True
        final.append("<")
        s = []
    elif S[i] == ">" :
        inTag = False
        final.append(''.join(s))
        final.append(">")
        s = []
    elif S[i] == " " :
        if inTag :
            s.append(" ")
        else :
            final.append(''.join(reversed(s)))
            final.append(" ")
            s = []
    else :
        s.append(S[i])

final.append(''.join(reversed(s)))
print(''.join(final))