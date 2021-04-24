'''
n = int(input().strip())
m = []
for i in range(n):
    m.append(list(map(int, input().strip().split())))

def zuidagongyueshu(x, a):
    for i in range(min(x, a), 0, -1):
        if x%i == 0 and a%i == 0:
            return i
    
def zuixiaogongbeishu(x, b):
    min_ = max(x, b)
    for i in range(1, 2000000000//min_+1):
        if (min_*i)%x == 0 and (min_*i)%b == 0:
            return min_*i

for i in range(n):
    count = 0
    for j in range(m[i][1], m[i][3]+1):
        if zuidagongyueshu(j, m[i][0]) == m[i][1] \
               and zuixiaogongbeishu(j, m[i][2]) == m[i][3]:
            count += 1
    print(count)
'''
from math import sqrt

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input().strip())

for i in range(n):
    a0, a1, b0, b1 = map(int, input().strip().split())
    ans = 0
    for j in range(1, int(sqrt(b1))+1):
        if b1 %j == 0:
            x = j
            if gcd(x, a0) == a1 and \
                   b0*x == b1*gcd(b0, x):
                ans += 1
            if j*j != b1:
                x = b1//j
                if gcd(x, a0) == a1 and \
                       b0*x == b1*gcd(b0, x):
                    ans += 1
    print(ans)
