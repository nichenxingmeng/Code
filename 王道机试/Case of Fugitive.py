MAX = 101
n, m = map(int, input().strip().split())

class Island:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Bridge:
    def __init__(self, length, index):
        self.length = length
        self.index = index

class Interval:
    def __init__(self, min_, max_, index):

        self.min_ = min_        
        self.max_ = max_
        self.index = index

def IntervalCompare(x, y):
    if x.min_ == y.min_:
        return x.max_ < y.max_
    else:
        return x.min_ < y.min_

def BridgeCompare(x, y):
    return x.length < y.length

island = [0] * n
bridge = [0] * m
interval = [0] * (n - 1)
ans = [0] * MAX

def Solve(n, m):
    pos = 0
    num = 0
    Q = []
    for i in range(m):
        while Q and Q[0].max_ < bridge[i].length:
            Q.pop(0)
        while pos < n - 1 and interval[pos].min_ <= bridge[i].length \
              and interval[pos].max_ >= bridge[i].length:
            Q.append(interval[pos])
            pos += 1
        if Q:
            current = Q.pop(0)
            ans[current.index] = bridge[i].index
            num += 1
    return num == n - 1

for i in range(n):
    left, right = map(int, input().strip().split())
    island[i] = Island(left, right)
for i in range(m):
    length = int(input().strip())
    bridge[i] = Bridge(length, i + 1)
for i in range(n - 1):
    interval[i] = Interval(island[i + 1].left - island[i].right, \
                                 island[i + 1].right - island[i].left, i)

interval.sort(key = lambda x: x.min_)
bridge.sort(key = lambda x: x.length)

if Solve(n, m):
    print("Yes")
    for i in range(n - 1):
        print(ans[i], end = ' ')
else:
    print("No")
