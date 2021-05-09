import sys
INF = sys.maxsize
N, M = map(int, input().strip().split())
MGraph = [[INF for _ in range(N)] for _ in range(N)]
for i in range(M):
    A, B, X = map(int, input().strip().split())
    MGraph[A][B] = X
    MGraph[B][A] = X
start, end = map(int, input().strip().split())
visit = [0 for _ in range(N)]
dist = [INF for _ in range(N)]

def dijkstra(n, s):
    dist[s] = 0

    for i in range(n):
        u = -1
        MIN =INF
        for j in range(n):
            if visit[j] == 0 and dist[j] < MIN:
                u = j
                MIN = dist[j]
        if u == -1:
            return -1

        visit[u] = 1

        for v in range(n):
            if visit[v] == 0 and MGraph[u][v] != INF:
                tmp = dist[u] + MGraph[u][v]
                if tmp < dist[v]:
                    dist[v] = tmp

dijkstra(N, start)
if dist[end] == INF:
    print('-1')
else:
    print(dist[end])
