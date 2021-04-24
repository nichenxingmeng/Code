n = int(input())
count = 0
m = input().strip()
while m != '':
    count += 1
    if count <= n:
        print(m)
        print()
    else:
        temp = m.split()
        for i in range(len(temp)):
            print(temp[i])
            print()
    m = input().strip()
