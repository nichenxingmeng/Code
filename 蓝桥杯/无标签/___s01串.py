n = int(input().strip())
s = ['0']
while n > 0:
    for i in range(len(s)):
        if s[i] == '0':
            s[i] = '1'
        else:
            s[i] = '01'
    while '01' in s:
        index_ = s.index('01')
        s[index_] = '0'
        s.insert(index_+1, '1')
    n -= 1
print(''.join(s))
