n = int(input().strip())

if n > 54:
    print('-1')
else:
    flag = False
    for i in range(10000, 999999):
        i = list(str(i))
        temp = i[:]
        if i == i[::-1]:
            for j in range(len(i)):
                i[j] = int(i[j])
            if sum(i) == n:
                flag = True
                print(''.join(temp))

    if not flag:
        print('-1')
