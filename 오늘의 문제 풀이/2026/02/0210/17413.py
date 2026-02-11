import sys
input = sys.stdin.readline

S = input().rstrip()

tag = False
answer = []
s = []
word = ""

for i in range(len(S)) :
    if S[i] == "<" :
        answer.append(''.join(reversed(s)))
        tag = True
        s = []
    elif S[i] == ">" :
        tag = False
        word += "<"+''.join(s)+">"
        s = []
    elif S[i] == " " :
        if tag == False :
            answer.append(''.join(reversed(s)))
            s = []
    else :
        s.append(S[i])

if s :
    answer.append(''.join(reversed(s)))

print(' '.join(answer))