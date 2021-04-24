n = int(input())
L = [1]
def loop(n):
    global L
    for i in range(len(L)):
        L[i] *= n
    for i in range(len(L)-1):
        L[i+1] += int(L[i]/10)
        L[i] = L[i]%10
    L1 = L[-1]
    L1 = list(str(L1))
    L.pop()
    for i in range(len(L1)-1,-1,-1):
        L.append(int(L1[i]))
        
for i in range(2,n+1):
    loop(i)
for i in range(len(L)-1, -1, -1):
    print(L[i], end='')
