m = int(input())
m = hex(m)
m = list(m)
for i in range(len(m)):
    if m[i] >= 'a' and m[i] <= 'z':
        m[i] = chr(ord(m[i])+ord('A')-ord('a'))
for i in range(2,len(m)):
    print(m[i], end='')
