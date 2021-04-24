v1, v2, t, s, l = map(int, input().split())
t20 = int(l/v2)
t2 = 0
L1 = 0
L2 = 0
count = 0
while L1 < l:
    L1 += v1
    L2 += v2
    if L1 < l:
        if L1-L2 >= t:
            L2 += v2*s
            count += s
    t2 += 1
t10 = t2+count
if t10 < t20:
    print('R')
    print(t10)
elif t10 > t20:
    print('T')
    print(t20)
else:
    print('D')
    print(t10)
    
