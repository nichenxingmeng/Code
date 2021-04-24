temp = list(map(int, input().strip().split()))
while temp:
    for j in range(len(temp)):
        print(chr(temp[j]), end = '')
    temp = list(map(int, input().strip().split()))
