s = list(input().strip())
s.insert(0, '(')
s.append(')')
while '|' in s:
    kuohao = []
    huo = []
    flag = False
    for i in range(len(s)):
        if s[i] == '(':
            flag = False
            kuohao.append(i)
        elif s[i] == 'x':
            continue
        elif s[i] == '|' and  not flag:
            flag = True
            huo.append(i)
        elif s[i] == '|' and  flag: 
            s[kuohao[-1]+1:i] = ''
            j = 0
            while j < max(huo[-1]-kuohao[-1]-1, i-huo[-1]-1):
                s.insert(kuohao[-1]+1, 'x')
                j += 1
            kuohao.pop()
            huo.pop()
            break
        elif s[i] == ')' and flag:
            s[kuohao[-1]:i+1] = ''
            j = 0
            while j < max(huo[-1]-kuohao[-1]-1, i-huo[-1]-1):
                s.insert(kuohao[-1], 'x')
                j += 1
            kuohao.pop()
            huo.pop()
            break
        else:
            s.pop(i)
            s.pop(kuohao[-1])
            kuohao.pop()
            break 
            
while '(' in s:
    s.remove('(')
while ')' in s:
    s.remove(')')
print(len(s))
