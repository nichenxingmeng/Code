from math import sqrt
n = int(input().strip())
count = 1
temp = 1299900

m = [True if i&1 else False for i in range(temp+1)]
m[2] = True
for i in range(2,int(sqrt(temp))+1):
   j = i
   if m[i]:
      while i*j <= temp:
         m[i*j] = False
         j += 1

count0 = 0

for i in range(2, temp+1):
   if m[i]:
      count *= i%50000
      count %= 50000
      count0 += 1
   if count0 == n:
      break

print(count)
         
'''import math
n = int(input())
i = 2
s = a

def check(n):
   if n%2 == 0:
      return n==2
   elif n%3 == 0:
      return n==3
   elif n%5 == 0:
      return n==5
   for p in range(7,int(math.sqrt(n))+1,2):
      if n%p == 0:
         return 0
   return 1
while n:
   if check(i):
      s *= i%50000
      s %- 50000
      n -= 1
   i += 1
print(s)'''
