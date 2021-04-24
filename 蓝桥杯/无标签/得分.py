s = input().strip()
count = 0
for i in range(len(s)):
    if i == 0:
        if s[i] == 'O':
            count += 1
            print(count, end='')
        else:
            count = 0
            print(count, end='')
    else:
        if s[i] == 'O':
            count += 1
            print(f'+{count}', end='')
        else:
            count = 0
            print(f'+{count}', end='')
