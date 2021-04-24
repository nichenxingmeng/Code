s = input().strip()

temp = []
max_ = 0
min_ = 1001
for i in range(len(s)):
    if s[i] not in temp:
        temp.append(s[i])
        count = s.count(s[i])
        if count > max_:
            max_ = count
        if count < min_:
            min_ = count

print(max_ - min_)
