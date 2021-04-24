n, m, k = map(int, input().strip().split())
digong = []
for i in range(n):
    digong.append([int(j) for j in input().strip().split()])
walk = [[1,0], [0,1]]

def dfs(u):
    global count, jiazhi, ans_, temp
    ux = u[0]
    uy = u[1]
    if ux == n - 1 and uy == m - 1:
        ans_.append(temp[:])
        return
    x = ux + walk[0][0]
    y = uy + walk[0][1]
    if x < n and y < m:
        temp.append(digong[x][y])
        dfs([x, y])
        temp = temp[::-1]
        temp.remove(digong[x][y])
        temp = temp[::-1]
    x = ux + walk[1][0]
    y = uy + walk[1][1]
    if x < n and y < m:
        temp.append(digong[x][y])
        dfs([x, y])
        temp = temp[::-1]
        temp.remove(digong[x][y])
        temp = temp[::-1]

ans_ = []
temp = []
dfs([0, 0])

def dfs_(x, last, ans__):
    global ans, count, max_, temp
    if x > last:
        if count == k:
            ans += 1
            ans %= 1000000007
        return
    if ans__[x] > max_:
        back = max_
        max_ = ans__[x]
        count += 1
        dfs_(x+1, last, ans__)
        max_ = back
        count -= 1
    dfs_(x+1, last, ans__)

ans = 0
for i in range(len(ans_)):
    ans_[i].insert(0, digong[0][0])
    count = 0
    temp = []
    max_ = min(ans_[i]) - 0.5
    dfs_(0, len(ans_[i])-1, ans_[i])
print(ans % 1000000007)
