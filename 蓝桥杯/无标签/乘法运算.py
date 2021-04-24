a, b = map(int, input().strip().split())
if a < 10:
    if b >= 10:
        print(' '*(len(str(a*b))-len(str(a))+1), a, sep='')
        print('×', b, sep='')
        print('━━')
        print(' '*(len(str(a*b))-len(str(b%10*a))), b%10*a, sep='')
        print(' '*(len(str(a*b))-len(str(b//10*a))-1), b//10*a, sep='')
        print('━━')
        print('{:>4}'.format(a*b))
    else:
        print(' '*(len(str(a*b))-len(str(a))+1),' ', a, sep='')
        print('× ', b, sep='')
        print('━━')
        print('{:>4}'.format(a*b))
else:
    if b >= 10:
        print(' '*(len(str(a*b))-len(str(a))), a, sep='')
        print('×', b, sep='')
        print('━━')
        print(' '*(len(str(a*b))-len(str(b%10*a))), b%10*a, sep='')
        print(' '*(len(str(a*b))-len(str(b//10*a))-1), b//10*a, sep='')
        print('━━')
        print('{:>4}'.format(a*b))
    else:
        print(' '*(len(str(a*b))-len(str(a))), a, sep='')
        print('×', b, sep='')
        print('━━')
        print('{:>4}'.format(a*b))
