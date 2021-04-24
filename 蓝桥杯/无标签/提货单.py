n = int(input().strip())
shangpin = []
for i in range(n):
    shangpin.append([j for j in input().strip().split()])

count = 0
for i in range(n):
    count += float(shangpin[i][1])*float(shangpin[i][2])

print('{:.6f}'.format(count))
