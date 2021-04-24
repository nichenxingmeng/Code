from math import log
n = int(input().strip())

def fenjie(n):
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
             s += f'2({fenjie(m[i])})+'
        s += f'2({fenjie(m[-1])})'
        return s
temp = fenjie(n)
temp = list(temp)
while '1' in temp:
    temp_ = temp.index('1')
    temp.pop(temp_-1)
    temp.pop(temp_-1)
    temp.pop(temp_-1)
print(''.join(temp))

