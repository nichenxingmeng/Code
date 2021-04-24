'''
n =int(input().strip())
m = []
for i in range(3):
    m.append(list(int(j) for j in input().strip().split()))
m[0].sort()
m[1].sort()
m[2].sort()

count = 0
for i in range(n):
    flag = False
    for j in range(n):
        if flag:
            for k in range(n):
                if m[2][k] > m[1][j]:
                    count += n - k
                    break
        elif m[1][j] > m[0][i]:
            flag = True
            for k in range(n):
                if m[2][k] > m[1][j]:
                    count += n - k
                    break
        
print(count)
'''

n = int(input().strip())
num = list(map(lambda x: sorted(x), \
                [list(map(int, input().strip().split())) for i in range(3)]))
res = 0

for i in range(n):
    index_0, index_1 = 0, 0
    for j in range(index_0, n):
        if num[1][j] > num[0][i]:
            index_0 = j
            for k in range(index_1, n):
                if num[2][k] > num[1][j]:
                    index_1 = k
                    res += n - k
                    break
print(res)
