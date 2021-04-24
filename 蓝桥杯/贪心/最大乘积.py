from copy import deepcopy
zushu = int(input().strip())
shu = [[[],[]] for _ in range(zushu)]
for i in range(zushu):
    fu = []
    shu[i][0] = list(map(int, input().strip().split()))
    shu[i][1] = list(map(int, input().strip().split()))
    for j in range(shu[i][0][0]):
        if shu[i][1][j] < 0:
            fu.append(shu[i][1][j])
            shu[i][1][j] = -1
    while -1 in shu[i][1]:
        shu[i][1].remove(-1)
    shu[i].append(fu)

for i in range(zushu):
    result = 1
    j = 0
    while j < shu[i][0][1]: 
        if shu[i][0][1] - j >= 2:
            if len(shu[i][1])==0 or (len(shu[i][1])==1 and len(shu[i][2])>=2):
                temp1 = min(shu[i][2])
                shu[i][2].remove(temp1)
                temp2 = min(shu[i][2])
                shu[i][2].remove(temp2)
                result *= temp1*temp2
                j += 2
            elif len(shu[i][2])==0 or (len(shu[i][2])==1 and len(shu[i][1])>=2):
                temp1 = max(shu[i][1])
                shu[i][1].remove(temp1)
                temp2 = max(shu[i][1])
                shu[i][1].remove(temp2)
                result *= temp1*temp2
                j += 2
            elif len(shu[i][1]) >= 2 and len(shu[i][2]) >= 2:
                if len(shu[i][1]) >= 3:
                    back1 = deepcopy(shu[i][1])
                    temp1 = max(shu[i][1])
                    shu[i][1].remove(temp1)
                    temp2 = max(shu[i][1])
                    shu[i][1].remove(temp2)
                    temp3 = max(shu[i][1])
                    temp7 = temp1 * temp2 * temp3
                    back2 = deepcopy(shu[i][2])
                    temp4 = min(shu[i][2])
                    shu[i][2].remove(temp4)
                    temp5 = min(shu[i][2])
                    shu[i][2].remove(temp5)
                    temp8 = temp5 * temp4 * temp1
                    if temp7 > temp8:
                        result *= temp1*temp2
                        shu[i][2] = deepcopy(back2)
                        j += 2
                    else:
                        result *= temp4*temp5
                        shu[i][1] = deepcopy(back1)
                        j += 2
                else:
                    back1 = deepcopy(shu[i][1])
                    temp1 = max(shu[i][1])
                    shu[i][1].remove(temp1)
                    temp2 = max(shu[i][1])
                    shu[i][1].remove(temp2)
                    temp1 = temp1 * temp2
                    back2 = deepcopy(shu[i][2])
                    temp3 = min(shu[i][2])
                    shu[i][2].remove(temp3)
                    temp4 = min(shu[i][2])
                    shu[i][2].remove(temp4)
                    temp2 = temp3*temp4
                    if temp1 > temp2:
                        result *= temp1
                        shu[i][2] = deepcopy(back2)
                        j += 2
                    else:
                        result *= temp2
                        shu[i][1] = deepcopy(back1)
                        j += 2
            else:
                temp1 = shu[i][1][0]
                temp2 = shu[i][2][0]
                result *= temp1*temp2
                j += 2
        else:
            if shu[i][1]:
                temp = max(shu[i][1])
                result *= temp
                j += 1
            else:
                temp = max(shu[i][2])
                result *= temp
                j += 1
    print(result)

