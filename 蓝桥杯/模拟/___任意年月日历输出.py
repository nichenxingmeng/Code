import calendar
n, m = map(int, input().strip().split())
if n < 2007:
    print('False')
else:
    a = calendar.monthrange(n, m)
    b = a[0]
    c = a[1]
    print('---------------------')
    print(' Su Mo Tu We Th Fr Sa')
    print('---------------------')
    if b != 6:
        k = b+1
        print(' '*3*k, end='')
    for i in range(1, c+1):
        if i < 10:
            print(' ', str(i), end='')
        else:
            print(' '+str(i), end='')
        if k == 6:
            k = -1
            print()
        k += 1
    if k == 0:
        print('---------------------')
    else:
        print()
        print('---------------------')

'''
import calendar
L=[int(i) for i in input().split()]
calendar.setfirstweekday(firstweekday=6)
cal=calendar.month(L[0],L[1])
L2=cal.split('\n')
print("---------------------")
print(' '+L2[1])
print("---------------------")
for i in L2[2:-1]:
    print(' '+i)
print("---------------------")
'''
