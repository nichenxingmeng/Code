import sys
INF = sys.maxsize

class Edge:
    def __init__(self, to_, length_):
        self.to = to_
        self.length = length_

def CriticalPath(n):
    for i in range(n):
        if indegree[i] == 0:
            node.append(i)
            earliest[i] = 1

    while node:
        u = node.pop(0)
        topology.append(u)
        for i in range(len(graph[u])):
            v = graph[u][i].to
            l = graph[u][i].length
            earliest[v] = max(earliest[u] + 1, earliest[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                node.append(u)

    for i in range(len(topology) - 1, -1, -1):
        u = topology[i]
        if len(graph[u]) == 0:
            latest[u] = earliest[u]

        for j in range(len(graph[u])):
            v = graph[u][j].to
            l = graph[u][j].length
            latest[u] = min(latest[u], latest[v] - 1)

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n)]
topology = []
node = []
earliest = [0 for _ in range(n)]
latest = [INF for _ in range(n)]
indegree = [0 for _ in range(n)]
for i in range(m):
    from_, to_, length = map(int, input().strip().split())
    graph[from_].append(Edge(to_, length))
    indegree[to_] += 1

CriticalPath(n)

ans = 0
ans = max(ans, max(earliest))
print(ans)
