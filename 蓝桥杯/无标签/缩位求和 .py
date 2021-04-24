s = input().strip()
s = list(s)
while len(s) > 1:
    count = 0
    for i in range(len(s)):
        count += int(s[i])
    s = list(str(count))[:]
print(''.join(s))
