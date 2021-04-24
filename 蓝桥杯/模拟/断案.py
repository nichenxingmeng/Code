temp = [0 for _ in range(4)]
temp_ = temp[:]
keneng = []
for i in range(4):
    temp[i] = 1
    keneng.append(temp)
    temp = temp_[:]

for i in range(4):
    count = 0
    now = keneng[i]
    if (now[1] == 0 and now[3] == 1) or (now[1] != 0 and now[3] != 1):
        count += 1
    if (now[1] == 0 and now[2] == 1) or (now[1] != 0 and now[2] != 1):
        count += 1
    if (now[0] == 0 and now[1] == 1) or (now[0] != 0 and now[1] != 1):
        count += 1
    if count == 3:
        print(chr(ord('A')+i))
