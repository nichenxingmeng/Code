'''
from copy import deepcopy
n = int(input().strip())
list_ = ['1','2','3','4','5','6','7','8','9']

ans = 0
for i in range(n):
    print(i)
    list__ = [0 for _ in range(9)]
    temp = list(str(i))
    flag = False
    for j in range(len(temp)):
        if list__[int(temp[j])-1] == 0:
            list__[int(temp[j])-1] = 1
        else:
            flag = True
            break
    back = deepcopy(list__)
    if not flag:
        remain = n - i
        for j in range(2, 10**(9-len(temp)-len(str(i)))):
            list__ = deepcopy(back)
            temp1 = list(str(j))
            temp2 = list(str(remain*j))
            for k in range(len(temp1)):
                if list__[int(temp[k])-1] == 0:
                    list__[int(temp[k])-1] = 1
                else:
                    break
            for k in range(len(temp2)):
                if list__[int(temp[k])-1] == 0:
                    list__[int(temp[k])-1] = 1
                else:
                    break
            if sum(list__) == 9:
                ans += 1
print(ans)
'''
from itertools import permutations
num_ = [0,1,2,3,4,5,6,7,8,9]

def len_(n):
    ans = 0
    while n != 0:
        n //= 10
        ans += 1
    return ans

def getnum(x, y, num):
    ans = 0
    for i in range(x, y+1):
        ans = ans * 10 + num[i]
    return ans

ans = 0
n = int(input().strip())
pailie = list(permutations(num_[1:]))
for i in range(len(pailie)):
    num_[1:] = pailie[i][:]
    for j in range(1, len_(n)+1):
        inter = getnum(1, j, num_)
        for k in range(j+1, 9):
            fz = getnum(j+1, k, num_)
            fm = getnum(k+1, 9, num_)
            if inter + fz / fm == n:
                ans += 1
print(ans)
