import sys
INF = sys.maxsize
MOD = 1e9 + 7

def CriticalPath(n):
    for i in range(1, n + 1):
        if indegree[i] == 0:
            node.append(i)
    totalTime = 0
    
    while node:
        u = node.pop(0)
        topology.append(u)
        for i in range(len(graph[u])):
            v = graph[u][i]
            earliest[v] = max(earliest[u] + length[u], earliest[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                node.append(v)
                totalTime = max(totalTime, earliest[v] + length[v])

    for i in range(len(topology) - 1, -1, -1):
        u = topology[i]
        if len(graph[u]) == 0:
            latest[u] = totalTime - length[u]

        for j in range(len(graph[u])):
            v = graph[u][j]
            latest[u] = min(latest[u], latest[v] - length[u])

    return totalTime

n, m = map(int, input().strip().split())
length = list(map(int, input().strip().split()))
length.insert(0, 0)
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
earliest = [0 for _ in range(n + 1)]
latest = [INF for _ in range(n + 1)]
node = []
topology = []
for i in range(m):
    from_, to_ = map(int, input().strip().split())
    graph[from_].append(to_)
    indegree[to_] += 1 

totalTime = CriticalPath(n)

ans = 1
for i in range(1, n + 1):
    ans *= latest[i] - earliest[i] + 1
    ans %= MOD
print(totalTime)
print(int(ans))
