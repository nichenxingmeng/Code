temp = list(input().strip())
while temp:
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    print(sum(temp))
    temp = list(input().strip())

