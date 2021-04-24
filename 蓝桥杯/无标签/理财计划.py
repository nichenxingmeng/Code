k, n, p = map(float, input().strip().split())
temp = k
def fuli(k, p):
    return k*(1+p)
count = 0
k = fuli(k, p)
while count < n-1:
    k = fuli(k+temp, p)
    count += 1
print('{:.2f}'.format(k-temp*n-0.005))
