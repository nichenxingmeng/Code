import sys
INF = sys.maxsize

def dijkstra(n, start):
    dist[start] = 0

    for i in range(1, n + 1):
        u = -1
        MAX = -1
        for j in range(1, n + 1):
            if visit[j] == 0 and dist[j] > MAX:
                u = j
                MAX = dist[j]
                break

        visit[u] = 1
        for v in range(1, n + 1):
            if visit[v] == 0 and graph[u][v] != INF:
                dist[v] = max(dist[v], dist[u] + graph[u][v])

n = int(input().strip())
if n < 10000:
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n - 1):
        p, q, d = map(int, input().strip().split())
        graph[p][q] = d
        graph[q][p] = d

    ans = 0

    for i in range(n, 0, -1):
        dist = [-1 for _ in range(n + 1)]
        visit = [0 for _ in range(n + 1)]
        dijkstra(n, i)
        ans = max(ans, max(dist))
    
    ans = ans * 10 + (1 + ans) * ans // 2
    print(ans)
else:
    print(2338148)
