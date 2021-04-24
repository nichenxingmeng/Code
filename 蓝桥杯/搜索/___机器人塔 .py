m, n = map(int, input().strip().split())
x = 0
while (x+1)*x//2 != m+n:
    x += 1
cnt = 0
ans = 0
p = [[0 for _ in range(501)] for _ in range(501)]

def dfs(cur):
    global cnt, ans
    if cnt > n or cur*(cur+1)//2-cnt > m:
        return
    if cur == x:
        ans += 1
        return
    for i in range(2):
        cnt_ = cnt
        cnt += i
        p[0][cur] = i
        for j in range(1, cur+1):
            p[j][cur-j] = p[j-1][cur-j]^p[j-1][cur-j+1]
            cnt += p[j][cur-j]
        dfs(cur+1)
        cnt = cnt_

dfs(0)
print(ans)
        
