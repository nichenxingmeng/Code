'''
s = list(input().strip())
count = 0
if s[0] != s[1]:
    count += 1
if s[-1] != s[-2]:
    count += 1
for i in range(1, len(s)-1):
    if s[i] != s[i-1] and s[i] != s[i+1]:
        count += 1

print(count//2+1)
'''
s = list(input().strip())
sl=['ABT','ATB','BAT','BTA','TAB','TBA']
min_ = len(s)

for i in range(6):
    a, b, t = sl[i][0], sl[i][1], sl[i][2]
    lena, lenb = s.count(a), s.count(b)
    ab, at = s[0:lena].count(b), s[0:lena].count(t)
    ba, bt = s[lena:lena+lenb].count(a), s[lena:lena+lenb].count(t)
    count = ab + at + bt + ba - min(ab, ba)
    if count < min_:
        min_ = count

print(min_)
