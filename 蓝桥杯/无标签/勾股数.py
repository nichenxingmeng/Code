import math
for i in range(3, 333):
    for j in range(i, 500):
        k = int(math.sqrt(i*i+j*j))
        if k == math.sqrt(i*i+j*j) and i+j+k <= 1000:
            print('{} {} {}'.format(i, j, k))
