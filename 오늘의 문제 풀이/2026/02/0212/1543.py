import sys
input = sys.stdin.readline

S = input().rstrip()
word = input().rstrip()
idx, cnt = 0, 0
# print(S.count(word))

while True :
    idx = S.find(word, idx)
    if idx != -1 :
        cnt += 1
        idx += len(word)
    else :
        break

print(cnt)