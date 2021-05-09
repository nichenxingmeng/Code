def TopologicalSort(n):
    for i in range(n):
        if InDegree[i] == 0:
            node.append(i)

    num = 0
    while node:
        u = node.pop(0)
        num += 1
        for i in range(len(graph[u])):
            v = graph[u][i]
            InDegree[v] -= 1
            if InDegree[v] == 0:
                node.append(v)

    return num == n

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n)]
InDegree = [0 for _ in range(n)]
node = []

for i in range(m):
    from_, to_ = map(int, input().strip().split())
    graph[from_].append(to_)
    InDegree[to_] += 1

if TopologicalSort(n):
    print('YES')
else:
    print('NO')
