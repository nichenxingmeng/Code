n = int(input())
m = []
for i in range(n):
    m.append(input().strip())
for i in range(n):
    if m[i] == 'WYS':
        print('KXZSMR')
    elif m[i] == 'CQ':
        print('CHAIQIANG')
    elif m[i] == 'LC':
        print('DRAGONNET')
    elif m[i] == 'SYT' or m[i] == 'SSD' or m[i] == 'LSS' or m[i] == 'LYF':
        print('STUDYFATHER')
    else:
        print('DENOMINATOR')
