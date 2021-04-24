import math
n = int(input().strip())
x = pow(2, n)-1
print(int(math.log10(2)*n)+1)
x = x % pow(10, 500)
temp = []
for i in range(500):
    temp.append(x % 10)
    x = x//10
for i in range(499, -1, -1):
    print(temp[i], end='')
    if i % 50 == 0:
        print()
