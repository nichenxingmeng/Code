n = int(input())
m = [[] for x in range(n)]
t = [0 for x in range(n)]
for i in range(n):
    m[i] = input().strip()
exam = int(input())
a = 0

DaDa = 0
while a < exam:
    for i in range(n):
        temp = list(input().strip().split())
        if temp[1] == 'DaDa':
            DaDa += int(temp[0])
        for i in range(n):
            if m[i] == temp[1]:
                t[i] += int(temp[0])
    chucun = t[:]
    t.sort(reverse = True)
    for i in range(len(t)):
        if t[i] == DaDa:
            print(i+1)
            break
    t = chucun[:]
    a += 1
