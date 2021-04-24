import sys
sys.setrecursionlimit(100000)

n = int(input().strip())

def f2(n):
    if n == 1:
        return 3
    elif n == 2:
        return 4
    elif n == 3:
        return 5
    else:
        return (f1(n-1)+3*f1(n-3)+2*f2(n-3)+3)

def f1(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n == 3:
        return 6
    else:
        return (f2(n-1)+2*f1(n-3)+5)

print(f1(n)%99999999)
print(f2(n)%99999999)
