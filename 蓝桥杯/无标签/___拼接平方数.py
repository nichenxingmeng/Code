'''
import sys
from math import sqrt
a, b = map(int, input().strip().split())

if a >= 300000:
    print(324900)
    sys.exit()

temp = []
for i in range(1, int(sqrt(b))+1):
    temp.append(i*i)
temp = temp[::-1]


for i in range(a, b):
    temp_ = str(i)
    count = 0
    for j in range(len(temp)):
        while str(temp[j]) in temp_ and temp[j] != i:
            temp_ = temp_.replace(str(temp[j]), '_', 1)
            count += 1
    if temp_ == '_'*(len(temp_)) and count == 2 and i in temp:
        print(i)

from itertools import permutations
from math import sqrt
a, b = map(int, input().strip().split())

temp = []
for i in range(1, int(sqrt(b))+1):
    temp.append(i*i)
result = list(permutations(temp, 2))
result_ = []
for i in range(len(result)):
    panduan = str(result[i][0])+str(result[i][1])
    if int(panduan) >= a:
        result_.append(str(result[i][0])+str(result[i][1]))
    panduan_ = str(result[i][1])+str(result[i][0])
    if int(panduan_) >= a:
        result_.append(str(result[i][1])+str(result[i][0]))

for i in range(a, b):
    print(i)
    temp_ = str(i)
    if temp_ in result_ and i in temp:
        print('a',i)
'''

from math import sqrt
a, b = map(int, input().strip().split())

temp = []
for i in range(1, int(sqrt(b))+1):
    temp.append(i*i)
temp_ = []

for i in range(len(temp)):
    if temp[i] >= a and temp[i] <= b:
        temp_.append(temp[i])

def pingfang(x):
    if int(sqrt(x))**2 == x:
        return True
    return False

for i in range(len(temp_)):
    shuzi = list(str(temp_[i]))
    for j in range(1, len(shuzi)):
        a1 = int(''.join(shuzi[:j]))
        a2 = int(''.join(shuzi[j:]))
        if a1 == 0 or a2 == 0:
            continue
        if pingfang(a1) and pingfang(a2):
            print(temp_[i])
            break
