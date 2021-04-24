class Edge:
    def __init__(self, from_, to_, length_):
        self.from_ = from_
        self.to_ = to_
        self.length_ = length_

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def join(x, y):
    x_ = find(x)
    y_ = find(y)
    if x_ != y_:
        if height[x_] < height[y_]:
            fa[x_] = y_
        elif height[x_] > height[y_]:
            fa[y_] = x_
        else:
            fa[y_] = x_
            height[x_] += 1
    return

def Kruskal(n, edgenum):
    edge.sort(key = lambda x: x.length_)
    sum_ = 0
    for  i in range(edgenum):
        cur = edge[i]
        if find(cur.from_) != find(cur.to_):
            join(cur.from_, cur.to_)
            sum_ += cur.length_
    return sum_

n = int(input().strip())
fa = [i for i in range(n + 1)]
height = [0 for _ in range(n + 1)]
edgenum = n * (n - 1) // 2
edge = [0 for _ in range(edgenum)]

for i in range(edgenum):
    x, y, z = map(int, input().strip().split())
    edge[i] = Edge(x, y, z)

ans = Kruskal(n, edgenum)
print(ans)
