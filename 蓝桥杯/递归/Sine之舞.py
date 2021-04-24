n = int(input())

def An(n, a):
    if a < n:
        if a % 2 == 1:
            print(f'sin({a}-',end='')
            An(n, a+1)
            print(')',end='')
        else:
            print(f'sin({a}+',end='')
            An(n, a+1)
            print(')',end='')
    elif a == n:
        print(f'sin({n})',end='')

def Sn(m, b):
    if b <= n:
        if b <n :
            print('(', end='')
        Sn(m-1, b+1)
        if b <n :
            print(')', end='')
        An(m ,1)
        print(f'+{b}', end='')

Sn(n,1)
