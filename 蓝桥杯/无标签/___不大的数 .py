'''
n = int(input().strip())
if n <= 1000000:
    print(''.join(list(str(pow(2, n)))[:10]))
else:
    if not n&1:
        m = [0 for _ in range(12)]
        temp = str(pow(2, n//2))
        for i in range(len(temp)):
            for j in range(len(temp)):
                if i+j <= 11:
                    m[i+j] += int(temp[i])*int(temp[j])
        for i in range(11, 0, -1):
            while m[i] >= 10:
                m[i-1] += m[i]//10
                m[i] %= 10
        if m[0] >= 10:
            for i in range(9):
                print(m[i], end='')
        elif m[0] == 0:
            for i in range(1, 11):
                print(m[i], end='')
        else:
            for i in range(10):
                print(m[i], end='')
    else:
        m = [0 for _ in range(12)]
        temp = str(pow(2, n//2))
        for i in range(len(temp)):
            for j in range(len(temp)):
                if i+j <= 11:
                    m[i+j] += 2*int(temp[i])*int(temp[j])
        for i in range(11, 0, -1):
            while m[i] >= 10:
                m[i-1] += m[i]//10
                m[i] %= 10
        if m[0] >= 10:
            for i in range(9):
                print(m[i], end='')
        elif m[0] == 0:
            for i in range(1, 11):
                print(m[i], end='')
        else:
            for i in range(10):
                print(m[i], end='')
'''
t = int(input().strip())
a = 1.0
while t > 0:
    a *= 2.0
    if a > 9999999999:
        a /= 10.0
    t -= 1
    
print(int(a))
