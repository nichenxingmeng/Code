n = int(input().strip())
if n >=0 and n < 10:
    print(n)
else:
    n = list(str(n))
    while '0' in n:
        n.remove('0')
    while len(n) > 1:
        temp = 1
        for i in range(len(n)):
            temp *= int(n[i])
        n = list(str(temp))
        while '0' in n:
            n.remove('0')
    print(n[0])
