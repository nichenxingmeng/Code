m = []
cnt = 0
ans = []
n = list(input().strip().split())

while n:
    cnt += len(n)
    for i in range(len(n)):
        m.append(n[i])
    if cnt == 52:
        break
    n = list(input().strip().split())

if cnt != 52:
    print('-1')
else:
    for i in range(52):
        if m[i] == 'J':
            temp = 11
        elif m[i] == 'Q':
            temp = 12
        elif m[i] == 'K':
            temp = 13
        else:
            temp = int(m[i])
        if temp <= len(ans):
            ans.insert(temp, m[i])
        else:
            ans.append(m[i])
    print(' '.join(ans))
