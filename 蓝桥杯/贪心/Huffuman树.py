n = int(input())
p = list(map(int,input().split()))

def find_min(cost):
    global p
    c = min(p)
    p.remove(c)
    d = min(p)
    p.remove(d)
    p.append(c+d)
    cost += c+d
    return cost

cost = 0
while len(p) > 1:
    cost = find_min(cost)
print(cost)
