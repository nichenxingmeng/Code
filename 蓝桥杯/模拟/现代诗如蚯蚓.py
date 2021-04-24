s = input().strip()
s = list(s)
max_ = 1

for i in range(1, len(s)+1):
    temp = []
    for j in range(0,len(s),i):
        temp.append(s[j:j+i])
    if max(temp) == min(temp):
        temp_ = len(temp)
        if temp_ >max_:
            max_ = temp_
print(max_)
