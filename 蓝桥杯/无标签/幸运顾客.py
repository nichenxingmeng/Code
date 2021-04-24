n = int(input().strip())
m = []
for i in range(n):
    m.append(int(input().strip()))
haoma = []

day = 0
for i in range(n):
    if m[i] > 0:
        haoma.append(m[i])
        haoma.sort()
    else:
        print(haoma[day])
        day += 1
