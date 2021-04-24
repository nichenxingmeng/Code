s = input().strip().split()
max_ = len(s[0])
for i in range(5):
    if len(s[i]) > max_:
        max_ = len(s[i])
for i in range(5):
    if len(s[i]) == max_:
        print(s[i])
