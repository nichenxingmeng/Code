def TopologicalSort(n):
    for i in range(1, n + 1):
        if indegree[i] == 0:
            node.append(i)
    
    while node:
        u = node.pop(0)
        ans.append(u)
        for i in range(len(graph[u])):
            v = graph[u][i]
            indegree[v] -= 1
            if indegree[v] == 0:
                node.append(v)
        node.sort()

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
node = []
ans = []

for i in range(m):
    from_, to_ = map(int, input().strip().split())
    graph[from_].append(to_)
    indegree[to_] += 1

TopologicalSort(n)
print(' '.join(map(str, ans)))
