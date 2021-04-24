n, m = map(int, input().strip().split())
count = n+m
for i in range(n):
    temp = '*'*(i+1)
    temp0 = '*'*i
    temp1 = ' '*m
    temp2 = '*'*(n-i+n-i-1)
    print('{:>{}}{}{}{}'.format(temp, count, temp0, temp1, temp2))
