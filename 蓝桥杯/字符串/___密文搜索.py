from itertools import permutations
s = input().strip()
n = int(input().strip())
m = []
for i in range(n):
    m.append(input().strip())
count = 0
for i in range(n):
    list_ = set(permutations(str(m[i]), 8))#permutations([x for x in range(5)], 5)
    for j in list_:
        temp = list(j)
        temp0 = temp[:]
        if ''.join(temp0) in s:
            count += 1
print(count)
