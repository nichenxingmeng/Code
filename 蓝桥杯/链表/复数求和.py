n = int(input().strip())
m = [[] for x in range(n)]
for i in range(n):
    m[i] = (input().strip().split())
counti = 0
countj = 0
for i in range(n):
    counti += int(m[i][0])
    countj += int(m[i][1])
print(f'{counti}+{countj}i')
