n = int(input().strip())
right = list(map(int, input().strip().split()))
m = []
test = list(map(int, input().strip().split()))
while test != [0 for x in range(n)]:
    m.append(test)
    test = list(map(int, input().strip().split()))
for i in range(len(m)):
    temp = []
    count1 = 0
    count2 = 0
    for j in range(n):
        if m[i][j] == right[j]:
            count1 += 1
            temp.append(m[i][j])
        elif  m[i][j] in right and m[i][j] not in temp:
            count2 += 1
    print(f'({count1},{count2})')
