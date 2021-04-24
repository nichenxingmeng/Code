p1, p2, p3 = map(int, input().strip().split())
s = list(input())
zimubiao = []
for i in range(26):
    zimubiao.append(chr(ord('a')+i))
zimubiao = ''.join(zimubiao)

def zhankai(p1, p2, p3):
    global s
    temp = -1
    for i in range(len(s)-1):
        if s[i] == '-':
            temp = i
            break
    if temp == 0:
        s[temp] = '+'
        return
    if temp == -1:
        s[temp] = '+'
        return
    if ord(s[temp-1]) + 1 == ord(s[temp+1]):
        s.pop(temp)
        return
    elif ord(s[temp-1]) >= ord(s[temp+1]):
        s[temp] = '+'
        return
    elif s[temp-1] in "0123456789" and s[temp+1] in "0123456789":
        if p1 == 3:
            result = '*'*((ord(s[temp+1])-ord(s[temp-1])-1)*p2)
        else:
            result = ''
            for i in range(ord(s[temp-1])+1, ord(s[temp+1])):
                result += chr(i)*p2
    elif s[temp-1] in zimubiao and s[temp+1] in zimubiao:
        if p1 == 3:
            result = '*'*((ord(s[temp+1])-ord(s[temp-1])-1)*p2)
        elif p1 == 1:
            result = ''
            for i in range(ord(s[temp-1])+1, ord(s[temp+1])):
                result += chr(i)*p2
            result = result.lower()
        else:
            result = ''
            for i in range(ord(s[temp-1])+1, ord(s[temp+1])):
                result += chr(i)*p2
            result = result.upper()
    else:
        s[temp] = '+'
        return
    if p3 == 2:
        result = list(result)
        result = result[::-1]
        result = ''.join(result)
    s[temp] = result
    return
        
while '-' in s:
    zhankai(p1, p2, p3)

for x in s:
    if x == '+':
        x = '-'
    print(x, end='')

