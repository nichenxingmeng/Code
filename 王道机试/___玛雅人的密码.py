n = int(input().strip())

s = list(input().strip())
t = 0

class item:
    def __init__(self, s, t):
        self.s = s
        self.t = t

Q = []
Q.append(item(s, t))

while Q:
    u = Q[0]
    Q.pop(0)
    
    if u.t > 10 ** 100:
        print(-1)
        flag = False
        break
    
    if '2012' in ''.join(u.s):
        print(u.t)
        break
    
    for i in range(n-1):
        x = u.s[:]
        
        temp = x[i + 1]
        x[i + 1] = x[i]
        x[i] = temp
        
        Q.append(item(x, u.t + 1))
