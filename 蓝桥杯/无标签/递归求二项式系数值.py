k, n = map(int, input().strip().split())

def f(k, n):
    if k == 0 or k == n:
        return 1
    return f(k, n-1) + f(k-1, n-1)

print(f(k, n))
