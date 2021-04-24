n = int(input().strip())

for i in range(1, n+1):
    if n % i == 0:
        print('{} * {} = {}'.format(i, n//i,n))
