n = int(input().strip())

def shengchengyuan(n):
    len_ = len(str(n))
    for i in range(1, 9*len_):
        temp = n-i
        if temp >= 0:
            temp = list(str(temp))
            for j in range(len(temp)):
                temp[j] = int(temp[j])
            if sum(temp)+n-i == n:
                return False
    return True

for i in range(1, n+1):
    if shengchengyuan(i):
        print(i)
