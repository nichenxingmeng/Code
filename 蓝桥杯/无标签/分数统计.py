n = int(input())
grade = list(map(int, input().strip().split()))
level = [[] for x in range(5)]
for i in range(len(grade)):
    if grade[i] >= 90:
        level[0].append(grade[i])
    elif grade[i] >= 80:
        level[1].append(grade[i])
    elif grade[i] >= 70:
        level[2].append(grade[i])
    elif grade[i] >= 60:
        level[3].append(grade[i])
    else:
        level[4].append(grade[i])

max = 0
temp = 0
for i in range(5):
    print(len(level[i]), end=' ')
    if len(level[i]) > max:
        max = len(level[i])
        temp = i
print()
print(len(level[temp]))
level[temp].sort(reverse = True)
for i in range(len(level[temp])):
    print(level[temp][i], end=' ')
