'''
n = int(input().strip())

class xiaopengyou:
    def __init__(self, index_, height_, bugaoxing_):
        self.index = index_
        self.height = height_
        self.bugaoxing = bugaoxing_

H = list(map(int, input().strip().split()))
H_ = [0 for _ in range(n)]

for i in range(n):
    H_[i] = xiaopengyou(i, H[i], 0)

flag = True
while flag:
    flag = False
    for i in range(n - 1):
        if H_[i].height > H_[i + 1].height:
            H_[i].bugaoxing += H_[i].bugaoxing + 1
            H_[i + 1].bugaoxing += H_[i + 1].bugaoxing + 1
            H_[i], H_[i + 1] = H_[i + 1], H_[i]
            flag = True

ans = 0
for i in range(n):
    ans += H_[i].bugaoxing

print(ans)
'''

'''
import sys
n = int(input().strip())

class xiaopengyou:
    def __init__(self, index_, height_, bugaoxing_):
        self.index = index_
        self.height = height_
        self.bugaoxing = bugaoxing_

H = list(map(int, input().strip().split()))
H_ = [0 for _ in range(n)]

for i in range(n):
    H_[i] = xiaopengyou(i, H[i], 0)

MIN = sys.maxsize
def dfs():
    global MIN
    flag = False
    for i in range(n - 1):
        if H_[i].height > H_[i + 1].height:
            flag = True
            break

    if not flag:
        cnt = 0
        for i in range(n):
            cnt += H_[i].bugaoxing
        MIN = min(MIN, cnt)
        return
    
    tmp = []
    for i in range(n - 1):
        if H_[i].height > H_[i + 1].height:
            tmp.append(i)
    
    for i in range(len(tmp)):
        back0 = H_[tmp[i]].bugaoxing
        back1 = H_[tmp[i] + 1].bugaoxing
        H_[tmp[i]].bugaoxing += H_[tmp[i]].bugaoxing + 1
        H_[tmp[i] + 1].bugaoxing += H_[tmp[i] + 1].bugaoxing + 1
        H_[tmp[i]], H_[tmp[i] + 1] = H_[tmp[i] + 1], H_[tmp[i]]
        dfs()
        H_[tmp[i]], H_[tmp[i] + 1] = H_[tmp[i] + 1], H_[tmp[i]]
        H_[tmp[i]].bugaoxing = back0
        back1 = H_[tmp[i] + 1].bugaoxing = back1

dfs()
print(MIN)
'''
'''
maxn = 1000010
tree = [0 for _ in range(maxn)]

def lowbit(x):
    return x & -x

def update(x, val):
    while x < maxn:
        tree[x] += val
        x += lowbit(x)

def query(x):
    ans = 0
    while x:
        ans += tree[x]
        x -= lowbit(x)
    return ans

n = int(input().strip())
A = list(map(int, input().strip().split()))
B = [0 for _ in range(n)]
for i in range(n):
    A[i] += 1
    B[i] = query(A[i])
    
    update(1, 1)
    update(A[i], -1)

tree = [0 for _ in range(maxn)]
for i in range(n - 1, -1, -1):
    B[i] += query(A[i])
    update(A[i] + 1, 1)

res = 0
for i in range(n):
    res += (B[i] + 1) * B[i] // 2
print(res)
'''
n = int(input().strip())
H = list(map(int, input().strip().split()))
A = [0 for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if H[j] < H[i]:
            A[i] += 1
    for j in range(i):
        if H[j] > H[i]:
            A[i] += 1

ans = 0
for i in range(n):
    if A[i] == 0:
        continue
    elif A[i] == 1:
        ans += 1
    else:
        ans += (1 + A[i]) * A[i] // 2

print(ans)
