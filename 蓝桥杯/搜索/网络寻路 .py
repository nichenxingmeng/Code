n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for i in range(1, n + 1):
    for j in range(len(graph[i])):
        u = graph[i][j]
        for k in range(len(graph[u])):
            v = graph[u][k]
            if v != i:
                ans += len(graph[v]) - graph[v].count(u)

print(ans)
