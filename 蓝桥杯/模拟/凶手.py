temp = [0 for _ in range(6)]
temp_ = temp[:]
result = []

for i in range(6):
    temp[i] = 1
    result.append(temp)
    temp = temp_[:]

for i in range(6):
    now = result[i]
    count = 0
    if now[0] == 0:
        count += 1
    if (now[0] == 1 or now[2] == 1):
        count += 1
    if now[0] == 0 and now[0] == 0 and now[2] == 0 and now[5] == 0:
        count += 1
    if count == 2:
        print(chr(ord('A')+i))
