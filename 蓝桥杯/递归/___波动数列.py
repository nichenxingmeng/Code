'''
import sys
sys.setrecursionlimit(100000)
from copy import deepcopy
n, s, a, b = map(int, input().strip().split())
temp = []

def jia():
    global temp
    temp.append(temp[-1]+a)

def jian():
    global temp
    temp.append(temp[-1]-b)

def dfs():
    global temp, count
    if len(temp) == n:
        if sum(temp) == s:
            count += 1
        return
    else:
        back = deepcopy(temp)
        jia()
        dfs()
        temp = deepcopy(back)
        jian()
        dfs()

count = 0
for i in range(-100, 100, 1):
    temp = [i]
    dfs()
print(count%100000007)
'''

n, s, a, b = map(int, input().strip().split())
sigma = (n - 1) * n // 2
dp = [0 for _ in range(sigma+1)]
do[0] = dp[1] = 1

for i in range(2, n):
    for j in range((i+1)*i//2, i-1, -1):
        dp[j] = (dp[j] + dp[j-1]) % 100000007

ans = 0
nx = s + sigma * b
unit = a + b
for i in range(sigma + 1):
    if nx % n == 0:
        ans = (ans + dp[i]) % 100000007
    nx -= unit

print(ans)
