import sys
sys.setrecursionlimit(100000)

zifu = input().strip()

def panduan(n):
    if (n >= 'a' and n <= 'z') or (n >= 'A' and n <= 'Z') \
           or n == '[' or n == ']':
        return False
    return True

i = 0
def expand():
    global i, zifu
    s = ''
    while i < len(zifu):
        if zifu[i] == '[':
            D = ''
            for j in range(i, len(zifu)):
                if panduan(zifu[i]):
                    D += zifu[j]
            i += 1 + len(D)
            D = int(D)
            X = expand()
            while D > 0:
                s += X
                D -= 1
        elif zifu[i] == ']':
            return s
        else:
            s += zifu[i]
        i += 1
    return s

print(expand())
