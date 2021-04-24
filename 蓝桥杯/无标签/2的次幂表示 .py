from math import log
n = int(input().strip())

def zhankai(n):
    if n <= 2:
        return n
    else:
        m = []
        s = ''
        temp = int(log(n, 2))
        for i in range(temp, -1, -1):
            if 2**i <= n:
                m.append(i)
                n -= 2**i
        for i in range(len(m)-1):
            s += f'2({zhankai(m[i])})+'
        s += f'2({zhankai(m[-1])})'
        return s
temp = zhankai(n)
temp = list(temp)
while '1' in temp:
    index_ = temp.index('1')
    for i in range(3):
        temp.pop(index_ - 1)
print(''.join(temp))
