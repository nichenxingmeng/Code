class Edge:
    def __init__(self, from_, to_, length, finish):
        self.from_ = from_
        self.to_ = to_
        self.length = length
        self.finish = finish

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

def Kruscal(num):
    sum_ = 0
    edge.sort(key = lambda x: x.length)
    for i in range(num):
        cur = edge[i]
        if fa[cur.from_] != fa[cur.to_]:
            join(cur.from_, cur.to_)
            sum_ += cur.length
    return sum_

n = int(input().strip())
fa = [_ for _ in range(n + 1)]
height = [0 for _ in range(n + 1)]
num = n * (n - 1) // 2
edge = [0 for _ in range(num)]

for i in range(num):
    a, b, c, d = map(int, input().strip().split())
    if d == 1:
        c = 0
    edge[i] = Edge(a, b, c, d)

ans = Kruscal(num)
print(ans)


