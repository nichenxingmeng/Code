from itertools import permutations
m = list(permutations([i for i in range(1,10)]))
for i in range(len(m)):
    if int(str(m[i][3])+str(m[i][4])+str(m[i][5])) == 2*int(str(m[i][0])+str(m[i][1])+str(m[i][2])):
        if int(str(m[i][6])+str(m[i][7])+str(m[i][8])) == 3*int(str(m[i][0])+str(m[i][1])+str(m[i][2])):
            for j in range(0,3):
                print(m[i][j], end='')
            print(' ', end='')
            for j in range(3,6):
                print(m[i][j], end='')
            print(' ', end='')
            for j in range(6,9):
                print(m[i][j], end='')
            print()
