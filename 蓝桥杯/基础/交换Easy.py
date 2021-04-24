n, m = map(int, input().strip().split())
s = list(map(int, input().strip().split()))
jiaohuan = [] 
for i in range(m):
    jiaohuan.append(list(map(int, input().strip().split())))
for i in range(len(jiaohuan)):
    s[jiaohuan[i][0]-1], s[jiaohuan[i][1]-1] = s[jiaohuan[i][1]-1], s[jiaohuan[i][0]-1]
for x in s:
    print(x)
