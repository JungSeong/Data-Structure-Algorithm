import sys
input = sys.stdin.readline

answer = []
S = input().rstrip()

for ch in S :
    if ch.isupper() :
        answer.append(chr((ord(ch)-ord('A')+13)%26+ord('A')))
    elif ch.islower() :
        answer.append(chr((ord(ch)-ord('a')+13)%26+ord('a')))
    else :
        answer.append(ch)
 
print(''.join(answer))