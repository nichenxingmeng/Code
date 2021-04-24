'''
from copy import deepcopy
n = int(input().strip())
lou = []
for i in range(n):
    lou.append(int(input().strip()))
lou_ = deepcopy(lou)

def shanchu(lou, index_):
    lou[index_] = 9999
    if index_-1 >= 0 and index_-1 < len(lou) and min(lou) != lou[index_-1]:
        lou[index_-1] = 9999
    if index_-2 >= 0 and index_-2 < len(lou) and min(lou) != lou[index_-2]:
        lou[index_-2] = 9999
    if index_+1 >= 0 and index_+1 < len(lou) and min(lou) != lou[index_+1]:
        lou[index_+1] = 9999
    if index_+2 >= 0 and index_+2 < len(lou) and min(lou) != lou[index_+2]:
        lou[index_+2] = 9999
    while 9999 in lou:
        lou.remove(9999)

if n <= 2:
    print(0)
else:
    count = 0
    while len(lou) >= 4:
        min_ = min(lou)
        count += min_
        index_ = lou.index(min_)
        shanchu(lou, index_)
    if len(lou) != 0:
        count += min(lou)

def shanchu_(lou, index_):
    lou[index_] = -1
    if index_-1 >= 0 and index_-1 < len(lou):
        lou[index_-1] = -1
    if index_-2 >= 0 and index_-2 < len(lou):
        lou[index_-2] = -1
    if index_+1 >= 0 and index_+1 < len(lou):
        lou[index_+1] = -1
    if index_+2 >= 0 and index_+2 < len(lou):
        lou[index_+2] = -1
    while -1 in lou:
        lou.remove(-1)

count_ = 0
while len(lou_) >= 4:
    min_ = min(lou_)
    count_ += min_
    index_ = lou_.index(min_)

    shanchu_(lou_, index_)
    if len(lou_) != 0:
        count_ += min(lou_)
print(count)
print(count_)
'''
n = int(input().strip())
lou = []
for i in range(n):
    lou.append(int(input().strip()))
lou.insert(0, 0)
dp = [0 for _ in range(n+1)]
dp_ = [0 for _ in range(n+1)]
dp[1] = lou[1]

for i in range(1, n+1):
    dp[i] = min(dp[i-1], dp_[i-1]) + lou[i]
    dp_[i] = min(dp[i-1], dp[i-2])

print(min(dp[n], dp_[n]))
