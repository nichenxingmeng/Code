'''
n, m = map(int, input().strip().split())
yingbi = [[1 for _ in range(m+1)] for _ in range(n+1)]

def fanzhuan(i, j):
    global yingbi
    if yingbi[i][j] == 0:
        yingbi[i][j] = 1
    else:
        yingbi[i][j] = 0

for x in range(1, n+1):
    for y in range(1, m+1):
        for i in range(1, n//x+1):
            for j in range(1, m//y+1):
                fanzhuan(i*x, j*y)

count_ = 0
for i in range(n):
    count_ += yingbi[i].count(0)
print(count_)
'''
'''
n, m = map(int, input().strip().split())

def numpy(n):
    if n == 1:
        return 1
    num = 0
    for i in range(2,n//2+1):
        if n % i == 0:
           num += 1
    return num+2

num = 0
for i in range(n+1):
    for j in range(m+1):
        if (numpy(i)*numpy(j))&1:
            num += 1
print(num)
'''
'''
from math import sqrt

n, m = map(int, input().strip().split())
a = int(sqrt(n))
b = int(sqrt(m))

print(a*b)
'''
#完全平方数有奇数个约数
#小于等于n的完全平方数的个数为[sqrt(n)]个
n, m = input().strip().split()

def dashuchengfa(s1, s2):
    num = [0 for _ in range(500)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            num[i+j+1] += int(s1[i])*int(s2[j])
    for i in range(len(s1)+len(s2)-1, 0, -1):
        if num[i] >= 10:
            num[i-1] += num[i]//10
            num[i] %= 10
    ans = ''
    if num[0] != 0:
        ans += str(num[0])
    for i in range(1, len(s1)+len(s2)):
        ans += str(num[i])
    return ans

def bijiao(s1, s2, pos):
    if len(s1) + pos != len(s2):
        return len(s1) + pos > len(s2)
    else:
        return s1 > s2

def dashu_sqrt(s):
    ans = []
    if len(s)&1:
        len_ = len(s)//2+1
    else:
        len_ = len(s)//2
    for i in range(len_):
        ans.append(0)
        for j in range(10):
            if bijiao(dashuchengfa(ans, ans), s, 2*(len_-1-i)):
                break
            ans[i] += 1
        ans[i] -= 1
    return ans

print(dashuchengfa(dashu_sqrt(n), dashu_sqrt(m)))
