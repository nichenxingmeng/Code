s1, s2 = map(str, input().strip().split())
if s1 == s2:
    print(0)
else:
    min_ = min(len(s1), len(s2))
    if min_ == len(s1):
        min_ = s1
    else:
        min_ = s2
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(min_)):
        if s1[i] != s2[i]:
            print(ord(s1[i]) - ord(s2[i]))
            break
