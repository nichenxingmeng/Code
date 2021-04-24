s = list(input().strip().split())
for i in range(len(s)):
    if s[i][-1] == ',' or s[i][-1] == '.':
        s[i] = list(s[i])
        s[i].pop()
        temp = ''
        for j in range(len(s[i])):
            temp += s[i][j]
        s[i] = temp
Len = len(s[0])
for i in range(len(s)):
    s[i] = s[i].lower()
    if len(s[i]) > Len:
        Len = len(s[i])
word = []
for x in s:
    if x not in word:
        word.append(x)
num = [0 for x in range(len(word))]
for i in range(len(word)):
    num[i] = s.count(word[i])

for i in range(len(word)):
    print(' '*(Len-len(word[i]))+word[i].upper()+':'+'*'*num[i]+str(num[i]))
