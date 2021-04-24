n, b = map(int, input().strip().split())
s = list(map(str, input().strip().split()))

i = 0
while i < len(s):
    if int(s[i]) % b == 0:
        s.remove(s[i])
        continue
    if int(s[i]) >= ord('A') and int(s[i]) <= ord('Z'):
        s[i] = chr(int(s[i]))
    i += 1

s.sort()
        
print(' '.join(s))
