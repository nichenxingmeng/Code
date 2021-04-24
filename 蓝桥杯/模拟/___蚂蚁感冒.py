'''
n = int(input().strip())
m = list(map(int, input().strip().split()))
temp = [False for _ in range(n)]
temp[0] = True

def pali():
    global m
    flag = True
    for i in range(len(m)):
        if abs(m[i]) > 0 and abs(m[i]) <100:
            flag = False
            break
    return flag

def panduan(n):
    if abs(n) > 0 and abs(n) < 100:
        return True
    else:
        return False

while not pali():
    for i in range(n):
        m[i] += 1
    print(m)
    for i in range(n):
        for j in range(i, n):
            if abs(m[i])==abs(m[j]) and i!=j and panduan(m[i]) and panduan(m[j]):
                m[i] = -m[i]
                m[j] = -m[j]
                if temp[i]:
                    temp[j] = True
                if temp[j]:
                    temp[i] = True
                for i in range(n):
                    m[i] += 1
                print(m)
                print(temp)

            elif ((abs(m[i])-abs(m[j])==1 and m[i]<0 and m[j]>0)or(abs(m[i])-abs(m[j])==-1 and m[i]>0 and m[j]<0)) and i != j and panduan(m[i]) and panduan(m[j]):
                m[i] = -m[i]-1
                m[j] = -m[j]-1
                if temp[i]:
                    temp[j] = True
                if temp[j]:
                    temp[i] = True
                for i in range(n):
                    m[i] += 1
                print(m)
                print(temp)
                
count = 0
for i in range(n):
    if temp[i]:
        count += 1
print(count)
'''

n = int(input().strip())
m = list(map(int, input().strip().split()))
temp = [False for _ in range(n)]
temp[0] = True

if m[0] > 0:
    for i in range(1, n):
        if abs(m[i]) > m[0] and m[i] < 0:
            temp[i] = True
    for i in range(1, n):
        if abs(m[i]) < m[0] and m[i] > 0:
            temp[i] = True
           
else:
    for i in range(1, n):
        if abs(m[i]) < abs(m[0]) and m[i] > 0:
            temp[i] = True
    for i in range(1, n):
        if abs(m[i]) > abs(m[0]) and m[i] < 0:
            temp[i] = True
    
count = 0
for i in range(n):
    if temp[i]:
        count += 1
print(count)
