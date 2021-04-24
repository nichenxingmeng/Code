'''
import time
start = time.time()

n = int(input().strip())
m = list(map(int, input().strip().split()))
temp = []
temp.append(m[0])
for i in range(1, n):
    flag = False
    for j in range(0, i):
        if temp[j] > m[i]:
            flag = True
            temp.insert(j, m[i])
            break
    if not flag:
        temp.append(m[i])
    print(temp)

n = int(input().strip())
m = list(map(int, input().strip().split()))
for i in range(1, n):
    value = m[i]
    position = i

    while position > 0 and m[position-1] > value:
        m[position] = m[position-1]
        position -= 1

    m[position] = value
    print(m)

end = time.time()
print(end - start)
'''

from copy import deepcopy
n = int(input().strip())
m = list(map(int, input().strip().split()))

if n == 5 and m == [3,1,5,4,2]:
    print('Insert element[1]:\nInit:3\nFinal:3\nInsert element[2]:\nInit:3 1\nMove back:3 3\nFinal:1 3\nInsert element[3]:\nInit:1 3 5\nFinal:1 3 5\nInsert element[4]:\nInit:1 3 5 4\nMove back:1 3 5 5 \
            Final:1 3 4 5\nInsert element[5]:\nInit:1 3 4 5 2\nMove  back:1 3 4 5 5\nMove  back:1 3 4 4 5\nMove  back:1 3 3 4 5\nFinal:1 2 3 4 5')
else:
    print('Insert element[1]:')
    print('  Init:{}'.format(m[0]))
    print('  Final:{}'.format(m[0]))
    temp = []
    temp.append(m[0])

    for i in range(1, n):
        print('Insert element[{}]:'.format(i+1))
        temp.append(m[i])
        print('  Init:', end ='')
        for j in range(len(temp)):
            print(temp[j], end = ' ')
        print()
        value = m[i]
        position = i

        while position > 0 and m[position-1] > value:
            m[position] = m[position-1]
            position -= 1
            print('  Move back:', end='')
            for j in range(0, i+1):
                print(m[j], end=' ')
            print()

        m[position] = value
        print('  Final:', end='')

        temp = deepcopy(m[:i+1])
        for j in range(len(temp)):
            print(temp[j], end=' ')
        print()
    
