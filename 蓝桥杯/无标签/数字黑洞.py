n = int(input().strip())
n = list(str(n))
def zhuanhuan():
    global n
    n.sort(reverse = True)
    ma = n[:]
    ma = int(ma[0])*1000+int(ma[1])*100+int(ma[2])*10+int(ma[3])
    n.sort()
    mi = n[:]
    mi = int(mi[0])*1000+int(mi[1])*100+int(mi[2])*10+int(mi[3])
    n = list(str(ma-mi))
    while len(n) < 4:
        n.insert(0, '0')
count = 0
while n != list(str(6174)):
    zhuanhuan()
    count += 1
print(count)


