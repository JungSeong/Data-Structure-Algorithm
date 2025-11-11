def dfs(n, visited, idx):
    if sum(visited) == n :
        start, link = 0, 0
        global S, answer

        teamStart = []
        teamLink = []

        for idx, i in enumerate(visited):
            if i == 1:
                teamStart.append(idx)
            else :
                teamLink.append(idx)

        for i in range(len(teamStart) - 1):
            for j in range(i + 1, len(teamStart)):
                A = teamStart[i]
                B = teamStart[j]
                start += S[A][B] + S[B][A]

        for i in range(len(teamLink) - 1):
            for j in range(i + 1, len(teamLink)):
                A = teamLink[i]
                B = teamLink[j]
                link += S[A][B] + S[B][A]

        answer.append(abs(link - start))
        return

    else:
        for i in range(idx, len(visited)):
            if visited[i] == 0:
                visited[i] = 1
                dfs(n, visited, i+1)
                visited[i] = 0

N = int(input())
S = []
answer = []

for i in range(N):
    elem = list(map(int, input().split()))
    S.append(elem)

visited = [0 for i in range(N)]
dfs(N/2, visited, 0)

print(min(answer))