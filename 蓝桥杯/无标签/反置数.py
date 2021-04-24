n, m = map(int, input().strip().split())

def daozhi(n):
    n = list(str(n))
    n = n[::-1]
    return int(''.join(n))

print(daozhi(daozhi(n)+daozhi(m)))
