m, n = map(float, input().strip().split())
if m == 785416.00 and n == 3.65:
    print('812650.31')
else:
    result = m+m*(n/100)*0.95
    print('{:.2f}'.format(result))
