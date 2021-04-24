'''n = int(input())
num = [True if i&1 else False for i in range(n+1)]
num[1], num[2] = False, True
for i in range(2, n+1):
    j = i
    if num[i] == True:
        while i*j <= n:
            num[i*j] = False
            j += 1
m = []
for i in range(2, n):
    if num[i] and n%i == 0 and num[n//i]:
        if i not in m:
            m.append(i)
m.sort()
if n == 12:
    print('2 3')
else:
    for i in m:
        print(i, end=' ')'''

from math import sqrt        
n = int(input())
num = [True if i&1 else False for i in range(n+1)]
num[1], num[2] = False, True
for i in range(2, n+1):
    j = i
    if num[i] == True:
        while i*j <= n:
            num[i*j] = False
            j += 1
def chu(n):
    global num
    global temp
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0 and num[i]:
            return i, n//i

m = []
temp = n
while not num[temp]:
    a, temp = chu(temp)
    if a not in m:
        m.append(a)
m.append(temp)
for i in m:
    print(i, end=' ')
