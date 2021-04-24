n = input().strip()
if n == '':
    n = input().strip()
n = int(n)
m = list(map(int, input().strip().split()))

while n:
    dp = [0 for _ in range(n)]
    dp[0] = m[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + m[i], m[i])
    print(max(dp))
    n = input().strip()
    if n == '':
        n = input().strip()
    n = int(n)
    m = list(map(int, input().strip().split()))
