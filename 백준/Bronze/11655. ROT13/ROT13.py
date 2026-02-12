import sys
input = sys.stdin.readline

answer = []
S = input().rstrip()

for ch in S :
    after = ord(ch)+13
    if ch.isupper() :
        if not ord('A')<=after<=ord('Z') :
            after -= 26
        answer.append(chr(after))
    elif ch.islower() :
        if not ord('a')<=after<=ord('z') :
            after -= 26
        answer.append(chr(after))
    else :
        answer.append(ch)

 
print(''.join(answer))