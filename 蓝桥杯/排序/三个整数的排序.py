s = list(map(int, input().strip().split()))
s.sort(reverse = True)
for i in range(len(s)-1):
    print(s[i], end=' ')
print(s[-1])
