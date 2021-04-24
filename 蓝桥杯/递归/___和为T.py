'''
from itertools import permutations
n = int(input().strip())
m = list(map(int, input().strip().split()))
sum_ = int(input().strip())
result = []

for i in range(1, n+1):
    temp_ = list(permutations(m, i))
    for j in range(len(temp_)):
        temp = list(temp_[j])
        if sum(temp) == sum_:
            result.append(temp)

      
for i in range(len(result)):
    set_ = set()
    for x in result[i]:
        set_.add(x)
    for j in range(len(result)):
        if i != j:
            set__ = set()
            for k in range(len(result[j])):
                set__.add(result[j][k])
            if set_ == set__:
                result[j] = [-9999]

while [-9999] in result:
    result.remove([-9999])

def panduan(result):
    global n
    global m
    if m[n-1] not in result:
        return True

count = len(result)
temp__ = []
while result:
    for i in range(len(result)):
        if panduan(result[i]):
            temp__.append(result[i])
            result.pop(i)
        n -= 1

for i in range(len(temp__)):
    for j in range(len(temp__[i])):
        print(temp__[i][j], end = ' ')
    print()
print(count)
'''

n = int(input().strip())
shu = list(map(int, input().strip().split()))
T = int(input().strip())

ans = 0
ans_ = []
for S in range(1 << n):
    cnt = 0
    a = [0 for _ in range(n)]
    for i in range(n):
        if S & (1 << i):
            a[cnt] = shu[i]
            cnt += 1
    if sum(a) == T and a[0] != 0:
        ans_.append(list(map(str, a[:cnt][:])))
        ans += 1

while ans_:
    for i in range(len(ans_)):
        if str(shu[n - 1]) not in ans_[i]:
            print(' '.join(ans_[i]))
            ans_[i] = 0
    while 0 in ans_:
        ans_.remove(0)
    n -= 1
print(ans)
        
