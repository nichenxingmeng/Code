from math import sqrt
n = int(input().strip())
temp = n

num = [1 for _ in range(n+1)]
num[2] = [1]
for i in range(2, int(sqrt(n))+1):
    j = i
    while j*i <= n:
        num[j*i] = 0
        j += 1

ans = []      
for i in range(2, n):
    if num[i]:
        while temp % i == 0:
            ans.append(i)
            temp = temp//i
if ans:
    print('{}='.format(n), end = '')
    for i in range(len(ans)-1):
        print(ans[i], end = '*')
    print(ans[-1])
else:
    print('{}={}'.format(n, n))
