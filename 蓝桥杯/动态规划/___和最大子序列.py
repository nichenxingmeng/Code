n = int(input().strip())
s = list(map(int, input().strip().split()))
max_ = s[0]

'''
for i in range(1, n+1):
    for j in range(n-i+1):
        temp = s[j:j+i]
        temp_ = sum(temp)
        if temp_ > max_:
            max_ = temp_

print(max_)
'''
'''
dp = [0 for x in range(100001)]
dp[0] = s[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+s[i], dp[i])
    max_ = max(dp[i], max_)
print(max_)
'''
sum_ = 0
for i in range(n):
    sum_ += s[i]
    if max_ < sum_:
        max_ = sum_
    if sum_ < 0:
        sum_ = 0
print(max_)
