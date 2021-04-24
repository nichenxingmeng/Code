def huiwen(n, s):
    t = []
    if n % 2 == 0:
        for i in range(26):
            if s.count(chr(ord('a')+i))%2 != 0:
                print('Impossible')
                return False
        return True
    else:
        for i in range(26):
            if s.count(chr(ord('a')+i))%2 != 0:
                t.append(chr(ord('a')+i))
            if len(t) > 1:
                print('Impossible')
                return False
        return True

def step(n, s, s1, count):
    for i in range(n//2):
        if s[i:].count(s[i]) != 1:
            temp = s1[:n-i].index(s[i])
            s1.pop(temp)
            count += temp
            s = s1[::-1]
        else:
            count += n//2 - i
            s[i] = []
            s1 = s[::-1]
    return count

n = int(input())
o = list(input().strip().split())
s = []
for i in range(n):
    s.append(o[0][i])
s1 = s[::-1]
count = 0
if huiwen(n, s):
    print(step(n, s, s1, count))
