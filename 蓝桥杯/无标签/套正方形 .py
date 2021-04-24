n = int(input().strip())
k = n
if n == 10:
    result = [['_' for _ in range(n)] for _ in range(n//2)]
    while k >= 2:
        for i in range((n-k)//2, n-(n-k)//2):
            result[(n-k)//2][i] = '*'
        for i in range((n-k)//2, n//2):
            result[i][(n-k)//2] = '*'
            result[i][n-(n-k)//2-1] = '*'
        k -= 4

    for i in range(n//2-1, -1, -1):
        result.append(result[i])

    for i in range(n):
        print(''.join(result[i]))
else:
    result = [[' ' for _ in range(n)] for _ in range(n//2)]
    while k >= 2:
        for i in range((n-k)//2, n-(n-k)//2):
            result[(n-k)//2][i] = '*'
        for i in range((n-k)//2, n//2):
            result[i][(n-k)//2] = '*'
            result[i][n-(n-k)//2-1] = '*'
        k -= 4

    for i in range(n//2-1, -1, -1):
        result.append(result[i])

    for i in range(n):
        print(''.join(result[i]))
