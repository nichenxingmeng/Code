n = int(input())
s = input().strip()
min_ = s
for i in range(len(s)):
    temp = s[i:len(s)]+s[0:i]
    if temp < min_:
        min_ = temp
print(min_)
