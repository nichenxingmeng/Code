'''import math
def zhishu(n):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        for i in range(11,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    else:
        return False
    return True
n = int(input())
sum = 0
for i in range(2,n+1):
    if i == 2 or i == 3 or i==5 or i==7:
        sum += i
    elif zhishu(i):
        sum += i
print(sum)'''

from math import sqrt
n = int(input())
nums = [True if i&1 else False for i in range(n+1)]
nums[2] = True
for i in range(2, int(sqrt(n))+1):
    j = i
    if nums[i]:
        while i*j <= n:
            nums[i*j] = False
            j += 1
ans = 0
for i in range(2, n+1):
    if nums[i]:
        ans += i
print(ans)
