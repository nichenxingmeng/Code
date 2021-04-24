import sys
sys.setrecursionlimit = 1000000
from math import sqrt

n = int(input().strip())
current = n
dp = [[] for _ in range(10000)]
dp[0] = [0]

def zhishu(n):
    flag = True
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            falg = False
            break
    return flag

def take(temp_):
    global current
    global dp
    temp = []
    if current > 0:
        if int(sqrt(current)) > 2:
            for i in range(2, int(sqrt(current))+1):
                if zhishu(i) and current % i == 0:
                    temp.append(i)
    if not temp:
        return
    for i in range(len(temp)):
        current -= 2*temp[i]
        for j in range(len(dp[temp_-1])):
            dp[temp_].append(dp[temp_-1][j] + temp[i])
        take(temp_ + 1)

take(1)
for i in range(len(dp)):
    if not dp[i]:
        count = i
        break
print(max(dp[i-1]))
