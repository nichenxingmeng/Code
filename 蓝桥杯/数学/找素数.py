from math import sqrt
L, R = map(int, input().strip().split())
m = [True if i&1 else False for i in range(int(sqrt(R))+2)]
m[1] = False
m[2] = True
for i in range(2, int(sqrt(len(m)))+1):
    j = i
    if m[i]:
        while j*i <= int(sqrt(R))+1:
            m[j*i] = False
            j += 1

result = [i for i in range(L, R+1)]

for i in range(2, len(m)):
    if m[i]:
        j = max(L//i, 2)
        while j*i <= R:
            if j*i in result:
                result[result.index(j*i)] = False
            j += 1
       
count = 0
for i in range(len(result)):
    if result[i]:
        count += 1
print(count)
