import sys
MAX = 105
INF = sys.maxsize
dist = [INF for _ in range(MAX)]
visit = [0 for _ in range(MAX)]

def visitCulture(n, index):
    c = culture[index]
    for i in range(1, n + 1):
        if culture[i] == c:
            visit[i] = 1

def dijkstra(n, s):
    dist[s] = 0

    for i in range(1, n + 1):
        u = -1
        MIN = INF
        for j in range(1, n + 1):
            if visit[j] == 0 and dist[j] < MIN:
                u = j
                MIN = dist[j]

        if u == -1:
            return

        visit[u] = 1
        visitCulture(n, u)

        for v in range(1, n + 1):
            if visit[v] == 0 and MGraph[u][v] != INF and \
                   Matrix[culture[u]][culture[v]] == 0:
                if dist[u] + MGraph[u][v] < dist[v]:
                    dist[v] = dist[u] + MGraph[u][v]

N, K, M, S, T = map(int, input().strip().split())

culture = [int(j) for j in input().strip().split()]
culture.insert(0, 0)       
        
Matrix = []
Matrix.append([0])
for i in range(1, K + 1):
    Matrix.append([int(j) for j in input().strip().split()])
    Matrix[i].insert(0, 0)
                    
MGraph = [[INF for _ in range(MAX)] for _ in range(MAX)]

for i in range(1, M + 1):
    u, v, d = map(int, input().strip().split())
    MGraph[u][v] = d
    MGraph[v][u] = d

dijkstra(N, S)

if dist[T] != INF:
    print(dist[T])
else:
    print(-1)
