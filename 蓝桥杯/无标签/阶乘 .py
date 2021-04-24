n = int(input().strip())

ans = 1
while n > 1:
    ans *= n
    n -= 1
ans = list(str(ans))
while ans[-1] == '0':
    ans.pop()
print(ans[-1])
