n = int(input().strip())
count = 0
for i in range(1, n+1):
    temp = list(str(i))
    count += temp.count('1')
print(count)
