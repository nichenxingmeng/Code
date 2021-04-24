n = int(input().strip())
m = []
max_x = -9999
max_y = -9999
min_x = 9999
min_y = 9999

for i in range(n):
    temp = list(map(int, input().strip().split()))
    if temp[0] > max_x:
        max_x = temp[0]
    if temp[0] < min_x:
        min_x = temp[0]
    if temp[1] > max_y:
        max_y = temp[1]
    if temp[1] < min_y:
        min_y = temp[1]
    m.append(temp)

def demo_point(m, x, y):
    flag = False
    j = n-1
    for i in range(n):
        if min(m[i][1], m[j][1]) < y and max(m[i][1], m[j][1]) >= y:
            t = m[i][0]+((y-m[i][1])/(m[i][1]-m[j][1]))*(m[i][0]-m[j][0])
            if t < x:
                flag = not flag
        j = i
    return flag
            
count = 0
for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        if demo_point(m, i, j) and demo_point(m, i+1, j) and \
               demo_point(m, i, j+1) and demo_point(m, i+1, j+1):
            count += 1
print(count)

