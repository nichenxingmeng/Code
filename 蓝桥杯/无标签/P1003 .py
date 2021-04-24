from copy import deepcopy
liebiao = input().strip().split()
juzi = input().strip().split()

liebiao_ = deepcopy(liebiao)
for i in range(len(liebiao_)):
    liebiao_[i] = list(liebiao_[i])
    liebiao_[i].sort()

for i in range(len(juzi)):
    juzi[i] = list(juzi[i])
    juzi[i].sort()

for i in range(len(liebiao_)):
    if liebiao_[i] in juzi:
        print(liebiao[i], end = ' ')
