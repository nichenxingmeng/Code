n, m = map(int, input().strip().split())
T = list(map(int, input().strip().split()))
T.sort()
place = [[] for _ in range(m)]

for i in range(m):
    place[i] = [_ for _ in range(i, n, m)]

count = 0
for i in range(m):
    for j in range(len(place[i])-1):
        count += T[place[i][j]]*(len(place[i])-j-1)

print(count'''+sum(T)''')
