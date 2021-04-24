s = list(input().strip())

def huo():
    global s
    flag0 = False
    for i in range(len(s)):  
        if s[i] == '(':
            left = i
            flag0 = True
        flag1 = False
        if s[i] == ')':
            right = i
            flag1 = True
            flag = False
            shuxian0 = ''.join(s[left+1:right][:])
            shuxian = shuxian0.split('|')
            if len(shuxian) >= 2:
                flag = True
            if not flag:
                s.pop(left)
                s.pop(right-1)
                return
            result = len(max(shuxian))
            s = s[:left]+s[right+1:]
            s.insert(left, 'x'*result)
            return                
    if not flag0:
        shuxian2 = ''.join(s[:])
        shuxian3 = shuxian2.split('|')
        result = len(max(shuxian3))
        s = ['x'*result]
        return
    if flag0 and not flag1:
        s.remove('(')
        return

while '|' in s:
    huo()
while '(' in s:
    s.remove('(')
while ')' in s:
    s.remove(')')
s = ''.join(s)
print(len(s))
