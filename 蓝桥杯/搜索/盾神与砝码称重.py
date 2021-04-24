n, m = map(int, input().strip().split())
weightn = list(map(int, input().strip().split()))
weightm = list(map(int, input().strip().split()))

def dfs(left, right, start):
    global flag
    if flag:
        return
    if left == right:
        flag = True
        return
    if start == n:
        return
    else:
        back_ = right
        right += weightn[start]
        dfs(left, right, start+1)
        right = back_
        back = left
        left += weightn[start]
        dfs(left, right, start+1)
        left = back
        dfs(left, right, start+1)

for i in range(len(weightm)):
    flag = False
    dfs(weightm[i], 0, 0)
    if flag:
        print('YES')
    else:
        print('NO')
