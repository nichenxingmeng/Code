n, t = input().strip().split()
n = int(n)
c = float(t)
m = []
for i in range(n):
    m.append(list(map(float, input().strip().split())))

m.sort(key = lambda x: x[1]/x[0], reverse = True)

count = 0
for i in range(n):
    if m[i][0] <= c:
        count += m[i][1]
        c -= m[i][0]
    else:
        count += c*(m[i][1]/m[i][0])
        break

print(count)
