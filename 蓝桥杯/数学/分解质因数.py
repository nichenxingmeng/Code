from math import sqrt
def sushu(a):
    global t
    a = int(a)
    for i in range(2,int(sqrt(a))+1):
        if a%i == 0:
            t.append(i)
            sushu(a/i)
            break
    t.append(a)

a, b = map(int, input().split())
for i in range(a,b+1):
    t = []
    sushu(i)
    if not t:
        t.append(i)
    t = t[:len(t)//2+1]
    print(f'{i}=',end='')
    for i in range(len(t)-1):
        print(t[i], end='*')
    print(t[-1])
