import sys
input = sys.stdin.readline

alphabet = input().rstrip()
answer = []

for ch in alphabet :
    if ch.isupper() :
        answer.append(ch.upper())
    else :
        answer.append(ch.lower())

print(''.join(answer))