s = input().strip()
d = {'C':12.01, 'H':1.008, 'O':16.00, 'N':14.01}
count = 0
for i in range(len(s)-1):
    if s[i] in d.keys():
        if ord(s[i+1]) >= ord('A') and ord(s[i+1]) <= ord('Z'):
            count += d[s[i]]
        else:
            count += d[s[i]]*int(s[i+1])
if s[len(s)-1] in d.keys():
    count += d[s[len(s)-1]]
print(count)
