from copy import deepcopy
m = [str(i) for i in range(256)]
temp = input().strip()
while temp:
    flag = True
    for i in range(3):
        temp_ = deepcopy(temp[:temp.index('.')])
        if temp_ not in m:
            flag = False
            break
        temp = deepcopy(temp[temp.index('.')+1:])
    if temp not in m:
        flag = False
    if flag:
        print('Y')
    else:
        print('N')
    temp = input().strip()
