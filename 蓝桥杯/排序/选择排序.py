n = int(input().strip())
s = list(map(int, input().strip().split()))

for i in range(0, n):
    num = i
    for j in range(i,n):
        if s[j] < s[num]:
            num = j
    s[num] , s[i] = s[i], s[num]
    print('swap(a[{}], a[{}]):'.format(i, num), end='')
    for j in range(len(s)):
        print(s[j], end=' ')
    print()
