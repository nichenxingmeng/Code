n = int(input().strip())
m = list(map(int, input().strip().split()))
for i in range(n+1):
    if m[i] != 0:
        if m[i] == 1:
            if i == 0:
                print(f'x^{n-i}', end='')
            elif i == n-1:
                print(f'+x', end='')
            elif i == n:
                print(f'+1', end='')
            else:
                print(f'+x^{n-i}', end='')
        elif m[i] == -1:
            if i == 0:
                print(f'-x^{n-i}', end='')
            elif i == n-1:
                print(f'-x', end='')
            elif i == n:
                print(f'-1', end='')
            else:
                print(f'-x^{n-i}', end='')
        else:
            if i == 0:
                print(f'{m[i]}x^{n-i}', end='')
            elif i == n-1:
                if m[i] > 0:
                    print(f'+{m[i]}x', end='')
                else:
                    print(f'{m[i]}x', end='')
            elif i == n:
                if m[i] > 0:
                    print(f'+{m[i]}', end='')
                else:
                    print(f'{m[i]}', end='')
            else:
                if m[i] > 0:
                    print(f'+{m[i]}x^{n-i}', end='')
                else:
                    print(f'{m[i]}x^{n-i}', end='')
