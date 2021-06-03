def CountNodes(m, n):
    if m > n:
        return 0
    else:
        return 1 + CountNodes(m * 2, n) + CountNodes(m * 2 + 1, n)

m, n = map(int, input().strip().split())
print(CountNodes(m, n))
