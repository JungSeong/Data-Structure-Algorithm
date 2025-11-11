import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
op = list(map(int, input().split()))
answer = list()

def dfs(l, op, cur, s):
    global answer
    if sum(op) == 0:
        answer.append(s)
        return
    else:
        for i in range(len(op)):
            if op[i] != 0:
                op[i] -= 1
                if i == 0:
                    dfs(l, op, cur + 1, s + l[cur])
                elif i == 1:
                    dfs(l, op, cur + 1, s - l[cur])
                elif i == 2:
                    dfs(l, op, cur + 1, s * l[cur])
                else :
                    if s < 0 :
                        dfs(l, op, cur + 1, -((-s) // l[cur]))
                    else :
                        dfs(l, op, cur + 1, s // l[cur])
                op[i] += 1

dfs(l, op, 1, l[0])
print(str(max(answer)) + "\n" + str(min(answer)))