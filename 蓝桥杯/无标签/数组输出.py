m = [[] for x in range(3)]
for i in range(3):
    m[i] = list(map(int, input().strip().split()))

ma = m[0][0]
x = 1
y = 1 
for i in range(3):
    for j in range(4):
        if abs(m[i][j]) > ma:
            ma = abs(m[i][j])
            x = i+1
            y = j+1
print(ma, x, y)
