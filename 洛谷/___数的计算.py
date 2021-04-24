n = int(input().strip())
f = [0 for _ in range(n+1)]

def sol(x):
    ans = 1
    if f[x]:
        return f[x]
    for i in range(1, x//2):
        ans += sol(i)
    f[x] = ans
    return ans

f[1] = 1
print(sol(n))
