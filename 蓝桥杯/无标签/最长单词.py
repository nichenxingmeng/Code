s = list(map(str, input().strip().split()))
ma = len(s[0])
temp = 0
for i in range(1, len(s)):
    if len(s[i]) > ma:
        ma = len(s[i])
        temp = i
print(s[temp])
