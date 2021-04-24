from math import sqrt
n = int(input().strip())
sum_ = n

nums = [True if i & 1 else False for i in range(n + 1)]
nums[1] = False
nums[2] = True
for i in range(2, int(sqrt(n))+1):
    j = i
    if nums[i]:
        while j * i <= n:
            nums[j * i] = False
            j += 1

zhi = []
for i in range(2, n+1):
    if sum_ == 0:
        break
    if nums[i]:
        while sum_ % i == 0:
            sum_ = sum_ // i
            zhi.append(i)

for i in range(len(zhi)-1):
    print(zhi[i], end = ' ')
print(zhi[-1])
print(len(zhi))   
