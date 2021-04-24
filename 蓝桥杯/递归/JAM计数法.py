from copy import deepcopy
s, t, w = map(int, input().strip().split())
Jam = list(input().strip())
xuanze = []

for i in range(s-1, t):
    xuanze.append(chr(ord('a')+i))

def dizeng(Jam):
    global xuanze
    if xuanze[len(xuanze)-w:] == Jam:
        return
    else:
        for j in range(-1, -w, -1):
            if Jam[j] != xuanze[j]:
                temp = deepcopy(Jam)
                for k in range(j, 0, 1):
                    Jam[k] = deepcopy(xuanze[xuanze.index(temp[j])+k-j+1])
                print(''.join(Jam))
                break

for i in range(5):
    dizeng(Jam)

