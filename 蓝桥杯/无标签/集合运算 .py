n = int(input().strip())
A = list(map(int, input().strip().split()))
m = int(input().strip())
B = list(map(int, input().strip().split()))

ans1 = []
if n < m:
    for i in range(n):
        if A[i] in B:
            ans1.append(A[i])
    ans1.sort()
    print(' '.join(map(str, ans1)))
else:
    for i in range(m):
        if B[i] in A:
            ans1.append(B[i])
    ans1.sort()
    print(' '.join(map(str, ans1)))

ans2 = set()
for i in range(n):
    ans2.add(A[i])
for i in range(m):
    ans2.add(B[i])
ans2 = list(ans2)
ans2.sort()
print(' '.join(map(str, ans2)))

for i in range(len(ans1)):
    A.remove(ans1[i])
A.sort()
print(' '.join(map(str, A)))
