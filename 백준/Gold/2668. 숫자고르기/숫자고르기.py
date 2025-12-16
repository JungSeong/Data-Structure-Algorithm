import sys
INPUT = sys.stdin.readline

N = int(INPUT())
adj = [0] * (N+1)

for i in range(1, N+1) :
    adj[i] = int(INPUT())

result = []

def dfs(node, start, visited) :
    visited[node] = True
    next_node = adj[node]

    if not visited[next_node] :
        dfs(next_node, start, visited)
    elif visited[next_node] and next_node == start :
        result.append(start)

for i in range(1, N+1) :
    visited = [False] * (N+1)
    dfs(i, i, visited)

print(len(result))
for col in result :
    print(col)