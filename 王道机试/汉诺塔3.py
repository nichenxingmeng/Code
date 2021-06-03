n = int(input().strip())

def hannuo(n):
    if n == 1:
        return 2
    else:
        return 3 * hannuo(n - 1) + 2

print(hannuo(n))
