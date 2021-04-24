from math import sqrt
n = int(input())
def phi(n):
    list0 = []
    for i in range(2, n+1):
        if n%i == 0:
            flag = True
            for j in range(2,int(sqrt(i))+1):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                list0.append(i)
    result = n
    for i in range(len(list0)):
        result *= 1-(1/list0[i])
    return int(result)
print(phi(n))
