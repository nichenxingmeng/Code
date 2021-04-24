'''
n, m = map(int, input().strip().split())
Ai = list(map(int, input().strip().split()))
m_ = m
Ai_ = Ai[:]

def xianglin(temp_):
    global Ai
    n = len(Ai)
    Ai[temp_-1] = -2005
    if temp_ != n-1:
        Ai[temp_+1] = -2005
    else:
        Ai[0] = -2005

def xianglin_(temp_):
    global Ai_
    n = len(Ai_)
    Ai_[temp_-1] = -2005
    if temp_ != n-1:
        Ai_[temp_+1] = -2005
    else:
        Ai_[0] = -2005
    
if 2*m > n:
    print("Error!")
else:
    count = 0
    while m > 0:
        temp = max(Ai)
        temp_ = Ai.index(temp)
        if temp_ == n-1:
            temp0 = Ai[temp_-1]+Ai[0]
        else:
            temp0 = Ai[temp_-1]+Ai[temp_+1]
        temp__ = temp
        temp___ = Ai[:]
        Ai[temp_] = -2005
        xianglin(temp_)
        temp1 = temp + max(Ai)
        if temp1 < temp0 and m>= 2:
            count += temp0
            m -= 2
            Ai = temp___[:]
            Ai[temp_-1] = -2005
            if temp_ == n-1:
                Ai[0] = -2005
            else:
                Ai[temp_+1] = -2005
            
            if temp_ == n-1:
                xianglin(0)
            else:
                xianglin(temp_+1)
            xianglin(temp_-1)
        else:
            count += temp__
            m -= 1

if 2*m_ > n:
    print("Error!")
else:
    count0 = 0
    while m_ > 0:
        temp = max(Ai_)
        temp_ = Ai_.index(temp)
        Ai_[temp_] = -2005
        xianglin_(temp_)
        count0 += temp
        m_ -= 1
    
print(count, count0)
'''
n, m = map(int, input().strip().split())
L = [int(_)+1001 for _ in input().strip().split()]
if n < 2*m:
    print('Error!')
else:
    re1 = [[0]*(n+1) for _ in range(m+1)]
    re2 = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(3, n+1):
            if i > j/2:
                re1[i][j] = 0
            else:
                re1[i][j] = max(re1[i][j-1], re1[i-1][j-2]+L[j-1])
    for i in range(1, m+1):
        for j in range(2, n+1):
            if i > j/2:
                re2[i][j] = 0
            else:
                re2[i][j] = max(re2[i][j-1], re2[i-1][j-2]+L[j-1])
    print(max(re1[m-1][n-1]+L[0], re2[m][n]) - m*1001)
