from copy import deepcopy

n = int(input().strip())
juzhen = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    i, j = map(int, input().strip().split())
    juzhen[i - 1][j - 1] = 1

def panduan(n, juzhen):
    for i in range(n):
        if juzhen[i][i] != 1:
            return False
    return True

def cheng(juzhen_, juzhen):
    juzhen__ = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += juzhen_[i][k] * juzhen[k][j]
            juzhen__[i][j] = tmp
    return juzhen__

if panduan(n, juzhen):
    print('1')
else:
    cnt = 1
    juzhen_ = deepcopy(juzhen)
    while not panduan(n, juzhen_):
        back = deepcopy(juzhen_)
        back_ = cnt
        juzhen_ = cheng(juzhen_, juzhen_)
        cnt *= 2
        if panduan(n, juzhen_):
            break
        back = deepcopy(juzhen_)
        back_ = cnt
        juzhen_ = cheng(juzhen_, juzhen)
        cnt += 1
        juzhen_ = cheng(juzhen_, juzhen_)
        cnt *= 2

    juzhen_ = deepcopy(back)
    for i in range(back_, cnt + 1):
        if panduan(n, juzhen_):
            ans = i
            break
        juzhen_ = cheng(juzhen_, juzhen)
        
    print(ans)  
