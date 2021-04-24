n = int(input().strip())
m = n
temp_ = 1
while n > 0:
    temp_ += m-n
    temp = temp_
    for i in range(n):
        print(temp, end = ' ')
        temp += 2+i+m-n
    print()
    n -= 1
