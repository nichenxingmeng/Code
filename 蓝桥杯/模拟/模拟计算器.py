a, b, c = map(str, input().strip().split())
if c == '+':
    print(int(a)+int(b))
elif c == '-':
    print(int(a)-int(b))
elif c == '*':
    print(int(a)*int(b))
elif c == '/':
    print(int(a)//int(b))
elif c == '%':
    print(int(a)%int(b))
