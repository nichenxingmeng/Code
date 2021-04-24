n = int(input().strip())
m = []
for i in range(n):
    m.append(int(input().strip()))
dp = [0 for _ in range(n)]
max_ = 0

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if m[i] == j + 1 and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    if max_ < dp[i]:
        max_ = dp[i]
print(max_)




































n = int(input().strip())
m = []
for i in range(n):
    m.append(int(input().strip()))
dp = [0 for x in range(n)]
max_ = 0

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if m[i] == j+1:
            dp[i] += 1
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    if max_ < dp[i]:
        max_ = dp[i]

print(max_)
