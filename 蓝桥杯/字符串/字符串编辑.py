s = list(input().strip())
def D(a):
    for i in range(len(s)):
        if s[i] == str(a):
            s.pop(i)
            return

def I(a1, a2):
    for i in range(len(s)):
        if s[i] == str(a1):
            temp = i
    s.insert(temp, str(a2))

def R(a1, a2):
    flag = False
    for i in range(len(s)):
        if s[i] == str(a1):
            s[i] = str(a2)
            flag = True
    if not flag:
        print('None')

m = list(input().strip().split())
if m[0] == 'D':
    D(m[1])
elif m[0] == 'I':
    I(m[1], m[2])
else:
    R(m[1], m[2])
for i in range(len(s)):
    print(s[i], end='')
