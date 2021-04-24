n, m, p = map(int, input().strip().split())
result = 1
n = n%p
while m > 0:
    if m&1:
        result = (result*n)%p
    m = m//2
    n = (n*n)%p
print(result)

'''
n, m, p = map(int, input().strip().split())
print(pow(n, m, p))
'''
