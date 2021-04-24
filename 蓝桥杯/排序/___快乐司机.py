n, w = map(int, input().strip().split())
m = []

for i in range(n):
    m.append(input().strip().split())

temp = []
for i in range(len(m)):
    temp.append(float(m[i][1])/float(m[i][0]))

temp.sort(reverse = True)
count = 0
value = 0

while count < w and temp:
    count_ = count
    for i in range(len(m)):
        if float(m[i][1])/float(m[i][0]) == temp[0]:
            temp_ = i
            break
    
    count += float(m[temp_][0])

    if count <= w:
        value += float(m[temp_][1])
    else:
        count = w
        value += (w-count_)*temp[0]
    temp.pop(0)
    m.pop(i)
    
print('{:.1f}'.format(value))
