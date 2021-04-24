n = int(input())
m0 = input().strip()
m1 = input().strip()
deng = [[1,1,1,1,1,1,0], [0,0,1,1,0,0,0], [0,1,1,0,1,1,1], [0,1,1,1,1,0,1], [1,0,1,1,0,0,1], [1,1,0,1,1,0,1], [1,1,0,1,1,1,1], [0,1,1,1,0,0,0], [1,1,1,1,1,1,1], [1,1,1,1,1,0,1]]
count = 0
for i in range(n):
    if m0[i] != m1[i]:
        for j in range(7):
            if deng[int(m0[i])][j] != deng[int(m1[i])][j]:
                count += 1
print(count)
