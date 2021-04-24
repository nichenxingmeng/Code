n = int(input().strip())
m = list(map(int, input().strip().split()))
cost = 0
while len(m) > 1:
    temp = m.index(min(m))
    cost += m[temp]*m[temp-1]*m[(temp+1)%(len(m))]
    m.pop(temp)
print(cost)
