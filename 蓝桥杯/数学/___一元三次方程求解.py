'''a, b, c, d = map(float, input().strip().split())

def fangcheng(x):
    return a*(x**3)+b*(x**2)+c*x+d

m = []
n = []
for i in range(-100, 101):
    m.append(abs(fangcheng(i)))
    n.append(i)

x = []
count = 0
while count < 3:
    temp = min(m)
    x.append(n[m.index(temp)])
    n.remove(n[m.index(temp)])
    m.remove(temp)
    count += 1

result = []
for i in range(3):
    min_ = abs(fangcheng(x[i]))
    min__ = x[i]
    for j in range(x[i]*100-50, x[i]*100+51):
        if abs(fangcheng(j/100)) < min_:
            min_ = abs(fangcheng(j/100))
            min__ = j/100
    result.append(min__)

result.sort()
for i in range(len(result)):
    print('{:.2f}'.format(result[i]), end=' ')'''
a, b, c, d = map(float, input().strip().split())
def f(x):
    return a*(x**3) + b*(x**2) + c*x + d

for i in range(-100, 100):
    l, r = i, i + 1
    flag = True
    while r-l > 10e-4:
        mid = (l+r)/2
        if f(l) == 0:
            print("{:.2f}".format(l), end=' ')
            flag = False
            break
        if f(mid) == 0:
            break
        if f(mid) * f(l) < 0:
            r = mid
        elif f(mid) * f(r) < 0:
            l = mid
        else:
            flag = False
            break
    if flag:
        print('{:.2f}'.format(mid), end = ' ')
