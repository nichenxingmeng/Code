import sys
INF = sys.maxsize
n, m = map(int, input().strip().split())
MGraph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
MGraph_ = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    a, b, d, p = map(int, input().strip().split())
    MGraph[a][b] = d
    MGraph_[a][b] = p
    MGraph[b][a] = d
    MGraph_[b][a] = p
start, end = map(int, input().strip().split())
dist = [INF for _ in range(n + 1)]
val = [INF for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

def dijkstra(n, s):
    dist[s] = 0
    val[s] = 0

    for i in range(1, n + 1):
        u = -1
        MIN =INF
        MIN_ = INF
        for j in range(1, n + 1):
            if visit[j] == 0 and dist[j] <= MIN:
                back = u
                back_ = MIN_
                u = j
                MIN = dist[j]
                MIN_ = val[j]
                if MIN_ > back_:
                    u = back
                    MIN_ = back_
        if u == -1:
            return -1
    
        visit[u] = 1

        for v in range(1, n + 1):
            if visit[v] == 0 and MGraph[u][v] != INF:
                tmp = MGraph[u][v] + dist[u]
                tmp_ = MGraph_[u][v] + val[u]
                if tmp <= dist[v]:
                    dist[v] = tmp
                    val[v] = min(tmp_, val[v])

dijkstra(n, start)
print(dist[end], val[end])
