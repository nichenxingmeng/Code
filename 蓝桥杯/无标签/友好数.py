from math import sqrt
a, b = map(int, input().strip().split())
count1 = 1
count2 = 1
for i in range(2, int(sqrt(a))+1):
    if a % i == 0:
        count1 += i
        count1 += a//i
for i in range(2, int(sqrt(b))+1):
    if b % i == 0:
        count2 += i
        count2 += b//i

if count1 == b and count2 == a:
    print('yes')
else:
    print('no')
