n = int(input())
m = [0 for x in range(n)]
for i in range(n):
    m[i] = input().strip()
name = []
for i in range(n):
    if m[i] not in name:
        name.append(m[i])
num = [0 for x in range(len(name))]
for i in range(len(name)):
    num[i] = m.count(name[i])
max_ =  max(num)
result = []
for i in range(len(num)):
    if num[i] == max_:
        result.append(i)
result_ = []
for i in range(len(result)):
    result_.append(name[result[i]])
result_.sort()
for i in range(len(result_)):
    print(result_[i])
