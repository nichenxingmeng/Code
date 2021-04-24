n = 16
ans = 0
b1 = [[0 for _ in range(5)] for _ in range(5)]
b2 = [[0 for _ in range(5)] for _ in range(5)]
b3 = [[0 for _ in range(5)] for _ in range(5)]
a = [0 for _ in range(17)]

def dfs(x):
    if x > n:
        ans += 1
        for i in range(1, n+1):
            print(a[i], end = '')
            if i % 4 == 0:
                print()
        print()
        return
    row = (x-1)//4+1
    col = (x-1)%4+1
    block = (row-1)//2*2+(col-1)//2+1
    for i in range(1, 5):
        if b1[row][i] == 0 and b2[col][i] == 0 and b3[block][i] == 0:
            a[x] = i
            b1[row][i] = 1
            b2[col][i] = 1
            b3[block][i] = 1
            dfs(x+1)
            b1[row][i] = 0
            b2[col][i] = 0
            b3[block][i] = 0

dfs(1)
print(ans)
