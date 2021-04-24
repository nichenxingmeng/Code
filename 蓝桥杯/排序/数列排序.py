n = int(input())
s = list(map(int, input().split()))
s.sort()
for x in s:
    print(x, end=' ')
