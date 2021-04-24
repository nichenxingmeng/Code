n = int(input().strip())
xuesheng = {}
for i in range(n):
    temp = list(map(str, input().strip().split()))
    xuesheng[temp[0]] = temp[2]
    xuesheng[temp[1]] = temp[2]
m = int(input().strip())
for i in range(m):
    temp = list(map(str, input().strip().split()))
    if xuesheng[temp[0]] == xuesheng[temp[1]]:
        print('N')
    else:
        print('Y')
