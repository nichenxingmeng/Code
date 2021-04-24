shuru = input().strip()

while shuru != '0':
    shuru = str(shuru)
    n, m = map(int, shuru.split())
    un = [_ for _ in range(n + 1)]

    def find(x):
        if un[x] == x:
            return x
        un[x] = find(un[x])
        return un[x]

    def join(x, y):
        x1 = find(x)
        y1 = find(y)
        if x1 != y1:
            un[x1] = y1

    for i in range(m):
        x, y = map(int, input().strip().split())
        join(x, y)

    ans = []
    for i in range(1, n + 1):
        temp = find(i)
        if temp not in ans:
            ans.append(un[i])

    print(len(ans) - 1)
    
    shuru = input().strip()
