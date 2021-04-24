s = input().strip()
m = []
shuzi = ['2','3','4','5','6','7','8','9','1','J','Q','K','A']
huase = ['d', 'c', 'h', 's']

temp = 0
for i in range(len(s)):
    if s[i] in huase:
        m.append(s[temp:i+1])
        temp = i+1

temp0 = []
for i in range(len(m)):
     temp0.append(huase.index(m[i][-1]))
temp0.sort()

temp1 = []
for i in range(len(temp0)):
    j = 0
    while j < len(m):
        if huase[temp0[i]] == m[j][-1]:
            temp1.append(m[j])
            m.pop(j)
            break
        j += 1

temp2 = []
for i in range(len(temp1)):
    temp2.append(shuzi.index(temp1[i][0]))
temp2.sort()

temp3 = []
for i in range(len(temp2)):
    j = 0
    while j < len(temp1):
        if shuzi[temp2[i]] == temp1[j][0]:
            temp3.append(temp1[j])
            temp1.pop(j)
            break
        j += 1
for x in temp3:
    print(x, end=' ')

