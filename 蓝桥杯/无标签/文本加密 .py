s = input().strip()

for x in s:
    if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
        if x == 'Z':
            print('a', end = '')
        elif x == 'z':
            print('A', end = '')
        else:
            print(chr(ord(x)+1), end = '')
    else:
        print(x, end = '')
