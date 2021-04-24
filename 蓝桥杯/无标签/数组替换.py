m, n = map(int, input().strip().split())
a = list(input().strip().split())
b = list(input().strip().split())
m1, n1 = map(int, input().strip().split())

temp = b[:n1][:]
a[m1:m1+n1] = temp[:]

for i in range(len(a)-1):
   print(a[i], end=',')
print(a[-1])
