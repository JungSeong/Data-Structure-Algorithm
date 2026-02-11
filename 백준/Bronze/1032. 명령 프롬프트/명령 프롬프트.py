import sys
input = sys.stdin.readline

N = int(input())
file_name = [input().rstrip() for _ in range(N)]
answer = []

for elem in list(map(set, zip(*file_name))) :
    if len(elem)>1 :
        answer.append('?')
    else :
        answer.append(*elem)

print(''.join(answer))