n = int(input().strip())
for i in range(n):
    flag = True
    count = i
    for j in range(len(str(i))):
        count += int(str(i)[j])
    if count == n:
        print(i)
        flag = False
        break
if flag:
    print(0)

