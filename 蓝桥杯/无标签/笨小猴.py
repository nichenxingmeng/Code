import math
s = input().strip()
m = [0 for x in range(26)]
for i in range(26):
    m[i] = s.count(chr(ord('a')+i))
while 0 in m:
    m.remove(0)
temp = max(m) - min(m)
def zhishu(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
if not zhishu(temp) or temp == 0 or temp == 1:
    print('No Answer')
    print(0)
else:
    print('Lucky Word')
    print(temp)
