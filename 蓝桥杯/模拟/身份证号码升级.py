s = input().strip()
xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
temp = ['1','0','x','9','8','7','6','5','4','3','2']

s = list(s)
s.insert(6, '1')
s.insert(7, '9')
count = 0
for i in range(len(s)):
    count += int(s[i])*xishu[i]
count = count % 11
s.append(temp[count])
print(''.join(s))
