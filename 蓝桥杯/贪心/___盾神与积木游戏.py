from time import time
start = time()
m = int(input().strip())

for i in range(m):
    tian = []
    n = int(input().strip())
    temp_ = []
    for j in range(n):
        tian.append(list(map(int, input().strip().split())))
        temp_.append(tian[j][1]-tian[j][0])
    temp = 0
    flag = True
    
    for j in range(len(temp_)):
        temp__ = min(temp_)
        if temp__ <= 0:
            temp += tian[temp_.index(temp__)][0]
            temp_[temp_.index(temp__)] = 100000
        elif temp__ <= temp:
            temp += tian[temp_.index(temp__)][0]
            temp_[temp_.index(temp__)] = 100000
        else:
            flag = False
            print('NO')
            break
    if flag:
        print('YES')
end = time()
print(end - start)
