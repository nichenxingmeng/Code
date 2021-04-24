'''import time
start = time.time()'''
from math import sqrt
n = int(input().strip())
count = 0

for i in range(1, int(sqrt(n))+1):
    if n%i == 0:
        count += i
        count += n//i
if count == 2:
    temp = count
else:
    temp = count - n
if temp == n:
    print('yes')
else:
    print('no')
'''end = time.time()
print(end-start)'''
